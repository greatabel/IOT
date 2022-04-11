# ROS (Robot Operating System)
roscore是向节点提供连接信息。ros每一个节点的消息是点对点传输的。 rosscore作用仅仅是如何找到其他节点

# talker终端运行
rosrun rospy_tutorials talker

另开一个终端
rosrun rospy_tutorials listener

rqt_graph

# roslunch
roslaunch rospy_tutorials talker_listener.launch

# tf坐标系
右手坐标系： x轴向前 y轴向左 z轴向上
