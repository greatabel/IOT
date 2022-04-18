#!/usr/bin/env python
# BEGIN ALL
# BEGIN SHEBANG
#!/usr/bin/env python
# END SHEBANG

# BEGIN IMPORT
import rospy
# END IMPORT

# BEGIN STD_MSGS
from std_msgs.msg import Int32
# END STD_MSGS


rospy.init_node('topic_latched_publisher')

# BEGIN PUB
pub = rospy.Publisher('counter_latched', Int32,  queue_size=1, latch=True)
# END PUB


# BEGIN LOOP
rate = rospy.Rate(2)

count = 0
while not rospy.is_shutdown():
    pub.publish(count*10)
    count += 1
    print('publish:', count)
    rate.sleep()
# END LOOP
# END ALL
