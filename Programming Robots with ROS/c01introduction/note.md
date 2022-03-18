# ROS (Robot Operating System)
目的在于：简化在大量不同种类机器人平台之间构建复杂和稳定的机器人行为

# 安装
http://wiki.ros.org/melodic/Installation/Ubuntu

# sudo apt update报错
http://www.noobyard.com/article/p-kxfgaukt-ob.html

sudo gedit /etc/apt/sources.list
文件中http://cn.archive.ubuntu.com/ubuntu/
替换为http://mirrors.163.com/ubuntu/
再次sudo apt-get update


# 安装过程问题sudo rosdep init出错常规方法都无效后解决办法记录：
sudo apt-get install ca-certificates

sudo c_rehash /etc/ssl/certs
sudo -E rosdep init
http://obgeqwh.top/sudo-rosdep-init-error/


# 检查ros版本
1、先在终端输入roscore
2、打开新终端，再输入，rosparam list
3、再输入rosparam get /rosdistro就能得到版本