#!/usr/bin/env python
# BEGIN ALL
#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
	print 'in latched callback:'
	print msg._connection_header
	print msg.data


rospy.init_node('counter_latched_subscriber')
sub = rospy.Subscriber('counter_latched', Int32, callback)

rospy.spin()