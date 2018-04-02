# IceCreamBaby_BBB_MotorDriver
ROS node that controls the motors on my custom robot named Ice Cream Baby

This file should be added as part of a ROS workspace on a Beagle Bone Black board (e.g. download to ~/catkin_ws/src)

This ROS node takes advantage of adafruit's BBIO library which makes interfacing with the GPIO and PWM pins on the Beagle Bone 
Black board 1000x easier than doing so from scratch in C++. I would reccommend using this unless you have a reason to do 
otherwise.
