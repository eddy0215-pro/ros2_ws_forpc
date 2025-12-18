#!/bin/bash
# ==============================================
# simple_bot.xacro → simple_bot.urdf 변환 스크립트
# ==============================================

source "/opt/ros/humble/setup.bash" --
source ~/ros2_ws_forpc/install/setup.bash

# 현재 스크립트 위치 기준 경로 계산
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
URDF_DIR="$SCRIPT_DIR/models"

XACRO_FILE="$URDF_DIR/simple_bot.xacro"
URDF_FILE="$URDF_DIR/simple_bot.urdf"
SDF_FILE="$URDF_DIR/simple_bot.sdf"

echo "🔧 XACRO → URDF 변환 시작..."
echo "입력 파일: $XACRO_FILE"
echo "출력 파일: $URDF_FILE"

# 변환 실행
ros2 run xacro xacro $XACRO_FILE -o $URDF_FILE

# 2️⃣ URDF → SDF
gz sdf -p "$URDF_FILE" > "$SDF_FILE"
cp "$SDF_FILE" "$URDF_DIR/simple_bot/model.sdf"

# model.config 생성
cat <<EOF > "$URDF_DIR/simple_bot/model.config"
<?xml version="1.0"?>
<model>
  <name>$MODEL_NAME</name>
  <version>1.0</version>
  <sdf version="1.7">model.sdf</sdf>
  <author>
    <name>Auto Generated</name>
    <email>none@example.com</email>
  </author>
  <description>Converted from URDF automatically using gz sdf</description>
</model>
EOF

if [ $? -ne 0 ]; then
    echo "❌ URDF → SDF 변환 실패"
    exit 1
fi

if [ $? -eq 0 ]; then
  echo "✅ 변환 완료!"
  echo "생성된 파일: $SDF_FILE"
  sleep 5   # ✅ URDF 생성 완료 대기
  ros2 launch urdf_tutorial display.launch.py model:=$URDF_FILE
  check_urdf $URDF_FILE
else
  echo "❌ 변환 실패! 파일 경로나 ROS2 설정을 확인하세요."
fi

