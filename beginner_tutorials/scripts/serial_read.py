#!/usr/bin/env python
import serial
import rospy
from std_msgs.msg import String
import time
import json
get_a = 0
get_b = 0
get_c = 0
get_d = 0

def callback(data):
    global get_a,get_b,get_c,get_d
    get = data.data
    json_acceptable_string = get.replace("'", "\"") #Converted JSON
    get = json.loads(json_acceptable_string) #JSON --> String
    get_a = get["a"]
    get_b = get["b"]
    get_c = get["c"]
    get_d = get["d"]
    #rospy.loginfo(rospy.get_caller_id() + "fromCira %s", get) 





if __name__ == "__main__":
    arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=.1)

    rospy.Subscriber('chatter', String, callback) #recieve some massage from chatter
    pub = rospy.Publisher('serial_read', String, queue_size=10)
    rospy.init_node('read_ser', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        str = '%s, %s, %s\n' %(get_a,get_b,get_c) #set string for communicate
        #rospy.loginfo(str)
        arduino.write(str)
        data = arduino.readline()[:-2]

        if data:
            hello_str = data
            rospy.loginfo(hello_str)
            pub.publish(hello_str) #publish serial data

rate.sleep()     
