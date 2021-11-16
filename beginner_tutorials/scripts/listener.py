#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber('chatter', String, callback) #via chatter topic
    #rospy.spin()

def talker_cira():
    pub = rospy.Publisher('toCira', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello cira %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        listener()
        talker_cira()
    except rospy.ROSInterruptException:
        pass
