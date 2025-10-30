#!/bin/bash

# 시스템 업데이트 및 필수 패키지 설치
sudo apt update && sudo apt install -y curl gnupg lsb-release

# ROS 키 다운로드 및 저장
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

# ROS 2 저장소 추가
echo "deb [signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# 저장소 업데이트
sudo apt update
``