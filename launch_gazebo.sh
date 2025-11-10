#!/bin/bash
# ===========================================
# simple_bot Gazebo 자동 실행 + 로봇 스폰 스크립트
# ===========================================

# 경로 설정
WORLD_PATH="/home/pi/ros2_ws_forpc/src/simple_bot/worlds/simple_map.world"
SDF_PATH="/home/pi/ros2_ws_forpc/src/simple_bot/urdf/simple_bot.sdf"

# ROS2 환경 로드
source /opt/ros/humble/setup.bash
source ~/ros2_ws_forpc/install/setup.bash

# 1️⃣ Gazebo 실행 (ROS2 연동 모드)
echo "🚀 Gazebo 실행 중..."
gazebo --verbose \
  -s libgazebo_ros_init.so \
  -s libgazebo_ros_factory.so \
  "$WORLD_PATH" &

GAZEBO_PID=$!

# 2️⃣ Gazebo 준비 확인 (ros2 topic list에 /clock 토픽이 올라올 때까지 대기)
sleep 60

# 3️⃣ 로봇 스폰
echo "🤖 simple_bot 스폰 중..."
#ros2 run gazebo_ros spawn_entity.py \
# -file "$SDF_PATH" \
# -entity simple_bot \
# -x 0 -y 0 -z 0.2

# 4️⃣ 완료 메시지
if [ $? -eq 0 ]; then
  echo "✅ simple_bot 스폰 완료!"
else
  echo "❌ 스폰 실패! URDF 또는 Gazebo 상태 확인 필요."
fi

