# ros2_ws_forpc

## Do Env setup
export GZ_SIM_RESOURCE_PATH=$GZ_SIM_RESOURCE_PATH:/home/pi/ros2_ws_forpc/src/simple_bot/models
export LIBGL_ALWAYS_SOFTWARE=1

## Make New Model

// Go to src and cmd below
gz model --new simple_bot_name

## Launch World
ign gazebo ./worlds/new_map.sdf
