import os
from urllib import unquote
from subprocess import Popen
import time


print('###########  Smart_Agricultural Autorun ############')
import getpass
username = getpass.getuser()
print('user : ', username)


time.sleep(3)


# 1 run ros core
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'source /opt/ros/melodic/setup.bash && roscore'])
time.sleep(3)

# 2 run gazebo world
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'source /opt/ros/melodic/setup.bash && source ~/catkin_ws/devel/setup.bash --extend && roslaunch turtlebot3_gazebo turtlebot3_world.launch  ;$SHELL'])
time.sleep(3)

#3 run rviz slam
Popen(["gnome-terminal", '-x' , 'bash', '-c' ,'source /opt/ros/melodic/setup.bash && source ~/catkin_ws/devel/setup.bash --extend &&roslaunch turtlebot3_slam turtlebot3_slam.launch  ;$SHELL'])
time.sleep(3)


import subprocess
import shlex
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print output.strip()
    rc = process.poll()
    return rc

time.sleep(3)
print('####### END #######')
