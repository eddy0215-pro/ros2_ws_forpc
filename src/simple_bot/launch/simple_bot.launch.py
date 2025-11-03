from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node

def generate_launch_description():
    # Gazebo 실행 (Factory 플러그인 포함)
    gazebo = ExecuteProcess(
        cmd=[
            'gazebo',
            '--verbose',
            '-s', 'libgazebo_ros_factory.so',
            '/home/pi/ros2_ws_forpc/src/simple_bot/worlds/simple_map.world'
        ],
        output='screen'
    )

    # Robot State Publisher
    state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='state_publisher',
        output='screen',
        parameters=[{'use_sim_time': True}],
        arguments=['/home/pi/ros2_ws_forpc/src/simple_bot/urdf/simple_bot.urdf']
    )

    # URDF 모델 Gazebo에 스폰 (3초 지연)
    spawn_robot = TimerAction(
        period=3.0,  # Gazebo가 완전히 시작될 때까지 기다림
        actions=[Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-file', '/home/pi/ros2_ws_forpc/src/simple_bot/urdf/simple_bot.urdf',
                '-entity', 'simple_bot',
                '-x', '0', '-y', '0', '-z', '0.1'
            ],
            output='screen'
        )]
    )

    return LaunchDescription([
        gazebo,
        state_publisher,
        spawn_robot
    ])
