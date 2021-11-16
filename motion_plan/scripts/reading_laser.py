#!/usr/bin/env python
import rospy

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import String

def clbk_laser(msg):
    #720 / 5 = 144
    regions = {
    'right':min(min(msg.ranges[0:143]),10),
    'fright':min(min(msg.ranges[144:287]),10),
    'front':min(min(msg.ranges[288:431]),10),
    'fleft':min(min(msg.ranges[432:575]),10),
    'left':min(min(msg.ranges[576:713]),10)
    }
    rospy.loginfo(regions)
    try:
        regions = str(regions)
        pub.publish(regions)
    except:
        rospy.loginfo("Error")
    #talker_cira(regions)

def main():
    global pub
    rospy.init_node('reading_laser')

    sub = rospy.Subscriber('scan', LaserScan, clbk_laser)
    pub = rospy.Publisher('toCira', String, queue_size=10)

    rospy.spin()
    #test
    


if __name__ == "__main__":
    main()
