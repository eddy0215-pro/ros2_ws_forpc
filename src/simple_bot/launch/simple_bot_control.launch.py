from launch import LaunchDescription
from launch_ros.actions import Node
import os
import yaml

def generate_launch_description():
    # Paths
    robot_description_path = os.path.join(
        os.getenv('HOME'), 'ros2_ws_forpc', 'models', 'simple_bot.xacro'
    )
    controllers_yaml_path = os.path.join(
        os.getenv('HOME'), 'ros2_ws_forpc', 'src', 'simple_bot', 'config', 'simple_bot_controllers.yaml'
    )

    # robot_description
    robot_description = os.popen(f"xacro {robot_description_path}").read()

    # controller YAML
    with open(controllers_yaml_path, 'r') as f:
        controller_params = yaml.safe_load(f)

    return LaunchDescription([
        # robot_state_publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        # ros2_control_node
        Node(
            package='controller_manager',
            executable='ros2_control_node',
            parameters=[controller_params, {'robot_description': robot_description}],
            output='screen'
        ),

        # joint_state_broadcaster
        Node(
            package='controller_manager',
            executable='spawner',
            arguments=['joint_state_broadcaster', '--controller-manager', '/controller_manager'],
            output='screen'
        ),

        # diff_drive_controller
        Node(
            package='controller_manager',
            executable='spawner',
            arguments=['diff_drive_controller', '--controller-manager', '/controller_manager'],
            output='screen'
        ),
    ])
