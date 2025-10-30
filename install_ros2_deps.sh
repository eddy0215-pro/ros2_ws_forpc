#!/bin/bash
# ==========================================
# ROS2 Humble + colcon + OpenCV 관련 의존 패키지 설치 스크립트 (Ubuntu 22.04용)
# 실행: ./install_ros2_deps_ubuntu2204.sh
# ==========================================

set -e  # 오류 발생 시 중단

echo "==> 패키지 목록 업데이트"
sudo apt update
sudo apt upgrade -y

echo "==> 필수 빌드 도구 설치"
sudo apt install -y build-essential cmake git wget curl unzip \
    python3-colcon-common-extensions python3-pip python3-rosdep python3-vcstool

echo "==> YOLO 모델 설치"
pip install ultralytics

echo "==> ROS2 Humble 데스크탑 및 의존 패키지 설치"
sudo apt install -y ros-humble-desktop python3-rosinstall-generator

echo "==> OpenCV 관련 패키지 설치"
sudo apt install -y libopencv-dev python3-opencv

echo "==> ROS2 카메라 관련 패키지 설치"
sudo apt install -y ros-humble-camera-calibration-parsers

echo "==> rosdep 초기화 및 업데이트"
sudo rosdep init || true
rosdep update

echo "==> 설치 완료!"
