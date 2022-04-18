# topic

# https://www.cxyzjd.com/article/sinat_16643223/113967512

构建package包：
cd /home/abel/learnROS/ROSWorkSpace/src
catkin_create_pkg basics std_msgs rospy roscpp

然后复制topic_publisher.py 到生成的baisc/src
chmod u+x topic_publisher.py 

cd /home/abel/learnROS/ROSWorkSpace

source devel/setup.bash 
rosrun basics topic_publisher.py

另开命令行:
rospic echo counter -n 50

发现某种类型消息的所有话题
rostopic find std_msgs/Int32

rosrun basics topic_subscriber.py


rostopic pub counter std_msgs/Int32 12345

