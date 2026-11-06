from launch import LaunchDescription
import launch
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.frontend.parse_substitution import get_package_share_directory
from launch.substitutions.path_join_substitution import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions.find_package import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    ros_gz_sim_pkg_path = get_package_share_directory('ros_gz_sim')
    gz_launch_path = PathJoinSubstitution([ros_gz_sim_pkg_path, 'launch', 'gz_sim.launch.py'])

    package_path = FindPackageShare('drone')
    #launch_path = PathJoinSubstitution([package_path, 'launch', 'drone_launch.py' ])


    return LaunchDescription([
        SetEnvironmentVariable(
            'GZ_SIM_RESOURCE_PATH',
            PathJoinSubstitution([package_path, 'drone_models']),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gz_launch_path),
            launch_arguments={
                'gz_args': PathJoinSubstitution([package_path, 'world_models/world.sdf']),
                'on_exit_shutdown': 'True'
            }.items(),
        ),

        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/example_imu_topic@sensor_msgs/msg/Imu@gz.msgs.IMU',],
            remappings=[('/example_imu_topic',
                '/remapped_imu_topic'),],
                output='screen'
        ),
    ])
