#!/usr/bin/env python
import rospy

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import String

def clbk_laser(msg):
    #720 / 5 = 144
    regions = [
        min(min(msg.ranges[0:143]),10),
        min(min(msg.ranges[144:287]),10),
        min(min(msg.ranges[288:431]),10),
        min(min(msg.ranges[432:575]),10),
        min(min(msg.ranges[576:713]),10)
    ]
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

    sub = rospy.Subscriber('m2wr/laser/scan', LaserScan, clbk_laser)
    pub = rospy.Publisher('toCira', String, queue_size=10)

    rospy.spin()


if __name__ == "__main__":
    main()
