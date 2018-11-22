#!/usr/bin/env python
import serial
import rospy
from std_msgs.msg import String

# To which topic on Willy we will publish
pubTopicName = 'angletracker_data'
subTopicName = 'angletracker_command'

# Init ROS components
rospy.init_node('topic_publisher')
rospy.init_node('topic_subscriber')
pubTopicInstance = rospy.Publisher(topicName, String ,queue_size=25)
subTopicInstance = rospy.Subscriber(subTopicName, String, ExecuteCommand);

# Init default values
topicMessage = ""

# Init serial components
socket = serial.Serial()
socket.baudrate = 19200
socket.port = '/dev/ttyACM0'
socket.timeout = 1
socket.open()

# Continous loop for publishing serial data
while not rospy.is_shutdown(): 
    topicMessage = socket.readline()
    topicMessage = topicMessage.rstrip()
    topicInstance.publish(topicMessage)
    print(topicMessage)
	
# Callback method to execute commands from the angletracker_command topic
def ExecuteCommand(msg)
	socket.write(msg.data.encode())
