
from ament_index_python.packages import get_package_share_directory
import os
import subprocess
from launch import LaunchDescription
from launch.descriptions import Executable
from launch.actions import DeclareLaunchArgument, ExecuteProcess,  RegisterEventHandler, ExecuteLocal
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution 
from launch_ros.actions import Node
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import (DeclareLaunchArgument, EmitEvent, ExecuteProcess,
                            LogInfo, RegisterEventHandler, TimerAction)
from launch.conditions import IfCondition
from launch.event_handlers import (OnExecutionComplete, OnProcessExit,
                                OnProcessIO, OnProcessStart, OnShutdown)
from launch.events import Shutdown
from launch.substitutions import (EnvironmentVariable, FindExecutable,
                                LaunchConfiguration, LocalSubstitution,
                                PythonExpression)
from launch import Action

import asyncio
import collections.abc
from typing import Any  # noqa: F401
from typing import cast
from typing import Dict  # noqa: F401
from typing import Iterable
from typing import List
from typing import Optional
from typing import Text
from typing import Tuple
from typing import Union
import warnings

child_pid = None
def generate_launch_description():
    global child_pid
    # param_config_arg = DeclareLaunchArgument(
    #     "config_path",
    #     default_value=PathJoinSubstitution((
    #         get_package_share_directory("mirte_telemetrix"),
    #         "config",
    #         "mirte_user_config.yaml",
    #     )),
    # )

    # 
    print("start", child_pid)
    if not child_pid:
        child_pid = os.fork()
    print(child_pid)
    if(child_pid):
        # parent
        print(child_pid)
        z = ExecuteProcess(
            cmd=["/bin/bash","-c",os.path.join(  get_package_share_directory("teleop_twist_keyboard"),
            "scripts",
            "waitClose.sh") + f" {child_pid}"],
        # )), str(child_pid)],
            output="screen",
        )
        return LaunchDescription([z])
    else:
        # child
        subprocess.run(["/bin/bash", "-c", "/opt/ros/humble/lib/teleop_twist_keyboard/teleop_twist_keyboard"] )
        os._exit(0)
        return 