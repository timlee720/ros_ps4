# ros_ps4
ROS & PS4 Controller for Jetson NX

## Make Sure You've Installed
* [ROS Melodic](http://wiki.ros.org/melodic/Installation)

## Configuration
* Create ROS Workspace
```bash
mkdir -p ~/bot_ws/src
cd ~/bot_ws/
catkin_make
source devel/setup.bash
```

* Create ROS Package && Git Clone ROS Serial Python
```bash
cd ~/bot_ws/src
catkin_create_pkg ps4_bot std_msgs rospy roscpp
git clone https://github.com/ros-drivers/rosserial.git
cd ~/bot_ws
catkin_make -j1
. ~/catkin_ws/devel/setup.bash
roscd ps4_bot 
mkdir scripts
```

* Install ROS Joy Package
```bash
sudo apt install ros-melodic-joy
sudo chmod a+rw /dev/input/js0
```

## ROS Run
* Put the python files into ~/bot_ws/src/ps4_bot/scripts folder
* Modify the CMakeLists.txt
```bash
cd ~/bot_ws/src/ps4_bot
vim CMakeLists.txt
```
* Add the following lines into the text file

From section "## Install ##"
```
catkin_install_python(
  PROGRAMS 
    scripts/mainControl.py
    scripts/rosPub.py
    scripts/velocityCalc.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```
Exit the file (Ctrl+X)
```bash
cd ~/bot_ws/src/ps4_bbot/scripts
chmod +x mainControl.py rosPub.py velocityCalc.py
cd ~/bot_ws
catkin_make -j1
source ./devel/setup.bash
```
* Run the files
```bash
roscore
rosparam set joy_node/dev "/dev/input/jsX" #(optional, tell the joy node which joystick device to use- the default is js0. )
rosrun joy joy_node
rosrun ps4_bot mainControl.py
```
