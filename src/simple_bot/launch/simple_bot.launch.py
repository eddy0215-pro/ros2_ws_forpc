from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, TimerAction
import os

def generate_launch_description():
    home = os.environ['HOME']
    urdf_sdf_path = os.path.join(home, 'ros2_ws_forpc/src/simple_bot/urdf/simple_bot.sdf')
    urdf_path = os.path.join(home, 'ros2_ws_forpc/src/simple_bot/urdf/simple_bot.urdf')
    world_path = os.path.join(home, 'ros2_ws_forpc/src/simple_bot/worlds/simple_map.world')

    # Gazebo 실행 (Spawn 서비스 포함)
    gazebo_process = ExecuteProcess(
        cmd=[
            'gazebo',
            '--verbose',
            world_path,
            '-s', 'libgazebo_ros_factory.so'
        ],
        output='screen'
    )

    # robot_state_publisher (ROS topic용)
    state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='state_publisher',
        output='screen',
        parameters=[{'use_sim_time': True}],
        arguments=[urdf_path]
    )

    # 로봇 SDF 모델 Gazebo에 스폰 (3초 대기 후 실행)
    spawn_robot_node = TimerAction(
        period=3.0,  # 3초 대기 후 실행
        actions=[
            Node(
                package='gazebo_ros',
                executable='spawn_entity.py',
                arguments=['-topic', '/robot_description', '-entity', 'simple_bot', '-x', '0', '-y', '0', '-z', '0.05'],
                output='screen'
            )
        ]
    )

    return LaunchDescription([
        gazebo_process,
        state_publisher_node,
        spawn_robot_node
    ])
