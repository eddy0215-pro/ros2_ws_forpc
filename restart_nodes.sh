#!/bin/bash
# =========================================
# ROS2 노드 종료 후 재실행 스크립트
# =========================================
# setup ros2 environment
source "/opt/ros/$ROS_DISTRO/setup.bash" --
source ~/ros2_ws/install/setup.bash

# --------------------------
# 1️⃣ 실행 중인 관련 ROS2 노드 종료
# --------------------------
echo "Stopping ROS2 nodes..."
pkill -f "yolo_node"

# --------------------------
# 2️⃣ 각 노드 재실행
# --------------------------
echo "Starting ROS2 nodes..."

# motor_node
ros2 run yolo_image_viewer yolo_node &

echo "All ROS2 nodes restarted."

