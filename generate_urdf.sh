#!/bin/bash
# ==============================================
# simple_bot.xacro → simple_bot.urdf 변환 스크립트
# ==============================================

source "/opt/ros/humble/setup.bash" --
source ~/ros2_ws_forpc/install/setup.bash

# 현재 스크립트 위치 기준 경로 계산
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
URDF_DIR="$SCRIPT_DIR/src/simple_bot/urdf"

XACRO_FILE="$URDF_DIR/simple_bot.xacro"
URDF_FILE="$URDF_DIR/simple_bot.urdf"

echo "🔧 XACRO → URDF 변환 시작..."
echo "입력 파일: $XACRO_FILE"
echo "출력 파일: $URDF_FILE"

# 변환 실행
ros2 run xacro xacro "$XACRO_FILE" -o "$URDF_FILE"

if [ $? -eq 0 ]; then
  echo "✅ 변환 완료!"
  echo "생성된 파일: $URDF_FILE"
  sleep 3   # ✅ URDF 생성 완료 대기
  ros2 launch urdf_tutorial display.launch.py model:=/home/pi/ros2_ws_forpc/src/simple_bot/urdf/simple_bot.urdf
else
  echo "❌ 변환 실패! 파일 경로나 ROS2 설정을 확인하세요."
fi

