#!/usr/bin/env python
import serial
import rospy
from std_msgs.msg import String



def main():
    arduino = serial.Serial('/dev/ttyACM0', 500000, timeout=.1)


    pub = rospy.Publisher('serial_read', String, queue_size=10)
    rospy.init_node('read_ser', anonymous=True)
    rate = rospy.Rate(500000) # 10hz
    while not rospy.is_shutdown():
	    while True:
                data = arduino.readline()[:-2]
		#arduino.write(b'hello')
                if data:
                    #data = '{'+data+'}'
                    hello_str = data
                    rospy.loginfo(hello_str)
                    pub.publish(hello_str)
                    rate.sleep()




if __name__ == "__main__":
    main()
