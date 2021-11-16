#!/usr/bin/env python
import rospy

from  geometry_msgs.msg import Twist
#from vel.msg import velx
from beginner_tutorials.msg import vel

def callback(data):

    msg = vel()
    vel_x = data.linear.x
    vel_w = data.angular.z
    msg.velx = vel_x
    msg.velw = vel_w
    pub.publish(msg)
    rospy.loginfo("I heard %s", msg)


def vel_listen():
    global pub
    rospy.init_node('vel_listen', anonymous = True)
    rospy.Subscriber('/cmd_vel', Twist, callback)
    pub = rospy.Publisher('toCira', vel, queue_size=10)
    rospy.spin()


if __name__ == '__main__':
    try:
        vel_listen()
    except:
        rospy.loginfo('Fail')
