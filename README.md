# Smart House
This project works as (Smart House Server), a server that serves clients who want to control their things in their places.

# How to use
1- clone this repository in embeded device.

2- for Linux base operationg systems, open /etc/rc.local as super user and add the follwing two lines at the end (before "exit 0" command):

python3 /home/pi/smarthouse/SmartHouseServer1.py & > /home/pi/Desktop/log1.txt 2>&1

python3 /home/pi/smarthouse/SmartHouseServer2.py & > /home/pi/Desktop/log2.txt 2>&1

* We assume that you clone the repository in "/home/pi" directory.

3- ewstart your embeded device.

4 enjoy.
