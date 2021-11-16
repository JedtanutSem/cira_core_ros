#!/usr/bin/env python

import tf
import rospy
def main():
    rospy.init_node("tf_listen")
    try:
        rospy.loginfo(listener.lookupTransform('/odom', '/base_link', rospy.Time(0)))
    except:
        rospy.loginfo('fail')

if __name__ == "__main__":

    try:
        main()
    except:
        rospy.loginfo("fai2")
