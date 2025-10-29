import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
from ultralytics import YOLO
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy

class YoloNode(Node):
    def __init__(self):
        super().__init__('yolo_node')
        self.bridge = CvBridge()
        self.model = YOLO('yolov8n.pt')  # YOLOv8 nano 모델
        
        # 카메라 이미지 구독
        self.subscription = self.create_subscription(
            Image,
            '/image_raw',
            self.listener_callback,
            10
        )

        qos = QoSProfile(depth=10,
                 reliability=ReliabilityPolicy.RELIABLE,
                 history=HistoryPolicy.KEEP_LAST)

        self.annotated_pub = self.create_publisher(Image, '/camera/image_annotated', qos)
        self.detection_pub = self.create_publisher(String, '/camera/detections', qos)

        self.get_logger().info('YOLO Image Viewer Node Ready!')

    def listener_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        # 영상 뒤집기 (수직+수평)
        frame = cv2.flip(frame, -1)  # -1: 수직+수평, 0: 수직, 1: 수평

        results = self.model(frame)
        annotated_frame = results[0].plot()  # YOLO 박스 시각화

        # 감지 결과 텍스트로 변환
        detection_texts = []
        for box in results[0].boxes:
            cls = self.model.names[int(box.cls)]
            conf = float(box.conf)
            detection_texts.append(f"{cls} ({conf:.2f})")

        if detection_texts:
            self.detection_pub.publish(String(data=", ".join(detection_texts)))

        # 주석된 이미지 퍼블리시
        img_msg = self.bridge.cv2_to_imgmsg(annotated_frame, encoding='bgr8')
        self.annotated_pub.publish(img_msg)

def main(args=None):
    rclpy.init(args=args)
    node = YoloNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
