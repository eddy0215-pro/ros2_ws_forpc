# ros2_ws_forpc

## Do Env setup
export GZ_SIM_RESOURCE_PATH=$GZ_SIM_RESOURCE_PATH:/home/pi/ros2_ws_forpc/src/simple_bot/models
export LIBGL_ALWAYS_SOFTWARE=1

## Map for ros2
gazebo --verbose /home/pi/ros2_ws_forpc/src/simple_bot/worlds/simple_map.world

## Make New Model

// Go to src and cmd below
gz model --new simple_bot_name

## Launch World
ros2 launch gazebo_ros gz_sim.launch.py world:=/home/pi/ros2_ws_forpc/src/simple_bot/worlds/simple_map.sdf
gz sim /home/pi/ros2_ws_forpc/src/simple_bot/worlds/simple_map.sdf