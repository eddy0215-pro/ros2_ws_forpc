# ros2_ws_forpc

## Do Env setup
export GZ_SIM_RESOURCE_PATH=$GZ_SIM_RESOURCE_PATH:/home/pi/ros2_ws_forpc/src/simple_bot/models
export LIBGL_ALWAYS_SOFTWARE=1

## Make New Model

## Launch World
ros2 launch gz_ros2_control_demos diff_drive_skc.launch.py

## ign topic list
ign topic -l