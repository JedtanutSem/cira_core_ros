#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import json

def callback(data):
    get = data.data
    json_acceptable_string = get.replace("'", "\"")
    get = json.loads(json_acceptable_string)
    get = get["a"]
    rospy.loginfo(rospy.get_caller_id() + "fromCira %s", get)

def cira_listen():
    rospy.init_node('subCira', anonymous = True)
    rospy.Subscriber('fromCira', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        cira_listen()
    except:
        rospy.loginfo("fail")
