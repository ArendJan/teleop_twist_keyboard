# teleop_twist_keyboard
Generic Keyboard Teleoperation for ROS

## Run

```sh
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Publishing to a different topic (in this case `my_cmd_vel`).
```sh
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=my_cmd_vel
```

## Usage

```
This node takes keypresses from the keyboard and publishes them as Twist
messages. It works best with a US keyboard layout.
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit
```

## Parameters
- `stamped (bool, default: false)`
  - If false (the default), publish a `geometry_msgs/msg/Twist` message.  If true, publish a `geometry_msgs/msg/TwistStamped` message.
- `frame_id (string, default: '')`
  - When `stamped` is true, the frame_id to use when publishing the `geometry_msgs/msg/TwistStamped` message.
- `keyboard_timeout (double, default: 0.5)`
  - timeout for keyboard input. When holding a key, the second key event will take some more time than the events after that. This will keep sending the original value for this timeout to not have a hiccup at the start. Will have the robot keep driving after a key release until the timeout.
- `rate (double, default:20)`
  - rate to send the cmd_vel with during the keyboard_timeout. While pressing a key, then the repeat-interval of your OS will set it at some rate (often 30+Hz)