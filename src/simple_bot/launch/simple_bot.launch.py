from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, TimerAction
import os

def generate_launch_description():
    home = os.environ['HOME']
    urdf_path = os.path.join(home, 'ros2_ws_forpc/src/simple_bot/urdf/simple_bot.urdf')
    world_path = os.path.join(home, 'ros2_ws_forpc/src/simple_bot/worlds/simple_map.world')

    # Gazebo 실행 (ROS2 플러그인 포함)
    gazebo_process = ExecuteProcess(
        cmd=[
            'gazebo',
            '--verbose',
            world_path,
            '-s', 'libgazebo_ros_init.so',
            '-s', 'libgazebo_ros_factory.so'
        ],
        output='screen'
    )

    # robot_state_publisher (URDF → /robot_description)
    state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='state_publisher',
        output='screen',
        parameters=[{'use_sim_time': True, 'robot_description': open(urdf_path).read()}]
    )

    # 로봇 스폰 (TimerAction으로 5초 대기 후 실행)
    spawn_robot_node = TimerAction(
        period=5.0,
        actions=[
            Node(
                package='gazebo_ros',
                executable='spawn_entity.py',
                arguments=[
                    '-topic', 'robot_description',
                    '-entity', 'simple_bot',
                    '-x', '0', '-y', '0', '-z', '0.05'
                ],
                output='screen'
            )
        ]
    )

    return LaunchDescription([
        gazebo_process,
        state_publisher_node,
        spawn_robot_node
    ])
