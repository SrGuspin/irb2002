import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    TimerAction,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

# Esto fue generado por claude :p

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    delay = LaunchConfiguration('delay')

    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Usar el reloj de simulacion (/clock) de Gazebo',
    )

    declare_delay = DeclareLaunchArgument(
        'delay',
        default_value='8.0',
        description='Segundos de espera antes de arrancar el nodo mover',
    )

    # 1) Incluye el launch original de turtlebot3_gazebo
    turtlebot3_gazebo_dir = get_package_share_directory('turtlebot3_gazebo')

    mundo_turtlebot3 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                turtlebot3_gazebo_dir,
                'launch',
                'turtlebot3_world.launch.py',
            )
        )
    )

    # 2) Tu nodo
    nodo_mover = Node(
        package='mi_paquete',
        executable='mover',
        name='mover',
        output='screen',
        emulate_tty=True,
    )

    # Se espera un poco para que Gazebo y el robot esten listos
    nodo_mover_retardado = TimerAction(
        period=delay,
        actions=[nodo_mover],
    )

    return LaunchDescription([
        declare_use_sim_time,
        declare_delay,
        mundo_turtlebot3,
        nodo_mover_retardado,
    ])