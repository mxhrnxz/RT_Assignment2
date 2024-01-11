
# Research Track1- 2nd Assignment
# By: Seyedehmehrnaz Amirkalali S6221007
In this repository lies a Python script serving as a pivotal ROS (Robot Operating System) node. It is adept at handling position and velocity data and also canceling the mission. Additionally it publishes a costum message containing robot's coordinate and velocity as requeted in this assignment.


## The assignment
The assignment consists of three sections below:

- Create a new package, in which you will develop three nodes:
- (a) A node that implements an action client, allowing the user to set a target (x, y) or cancel it. Try to use the
feedback/status of the action server to know when the target has been reached. The node also publishes the
robot's position and velocity as a custom message (x,y, vel_x, vel_z), by relying on the values published on the
topic /odom;
- (b) A service node that, when called, returns the coordinates of the last target sent by the user;
- (c) Another service node that subscribes to the robot’s position and velocity (using the custom message) and
implements a server to retrieve the distance of the robot from the target and the robot’s average speed.
- Create a launch file to start the whole simulation. Use a parameter to select the size of the averaging window of node (c)

## How to run

First, the package needs to be cloned: `git clone https://github.com/mxhrnxz/RT_Assignment2.git`

Secondly, the Xterm needs to be installed: `sudo apt-get -y install xterm`

Then all the Python files in the Script folder need to have permission to be executed. This can be achieved by running the command:`chmod +x node_a.py`

And lastly, to run the program use this command in the launch folder terminal: `roslaunch assignment_2_2023 assignment1.launch`
## Node A Flowchart
Here is the flowchart of Node A for a better understanding of the code.
![flowchart](https://github.com/mxhrnxz/RT_Assignment2/assets/108267018/5a79cad7-a0f7-43ac-83c1-9f008fa9870d)
## RQT Gragh
Here is the RQT graph of the whole project to see how the nodes interact with each other
![rqt](https://github.com/mxhrnxz/RT_Assignment2/assets/108267018/d40efa74-aeec-485f-a2d5-3017c5722b3f)
