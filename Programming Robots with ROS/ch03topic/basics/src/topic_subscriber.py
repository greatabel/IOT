#!/usr/bin/env python
# BEGIN ALL
#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
	print 'in callback:'
	print msg.data


rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('counter', Int32, callback)

rospy.spin()