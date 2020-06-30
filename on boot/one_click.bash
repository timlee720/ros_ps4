
sleep 1

sudo chmod 666 /dev/ttyUSB0
sudo chmod 666 /dev/ttyUSB1

sudo chmod 666 /dev/ttyACM0
sudo chmod 666 /dev/ttyACM1
sudo chmod 666 /dev/ttyACM2
sudo chmod 666 /dev/ttyACM3



#roscore &

sleep 1
cd /home/ubuntu/bot_ws
source /opt/ros/melodic/setup.bash
source /home/ubuntu/bot_ws/devel/setup.bash 
nohup roscore &
sleep 8

nohup rosrun joy joy_node &
sleep 5

nohup rosrun ps4_bot mainControl.py &

nohup rosrun rosserial_python serial_node.py /dev/ttyACM0 _baud:=57600 &
sleep 3

#nohup rosrun ps4_bot mainControl.py &
