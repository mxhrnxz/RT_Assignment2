#!/usr/bin/env python3

import rospy
import math
from assignment_2_2023.msg import dataa
from assignment_2_2023.srv import Ave_pos_vel, Ave_pos_velResponse


# Define a class for the service
class NodeThree:
    def __init__(self):
        # Initialize class
        rospy.init_node('info_service') 
        rospy.Service("info_service", Ave_pos_vel, self.values)
        rospy.Subscriber("/position_velocity", dataa, self.distance_velocity)
        self.averagevelx = 0
        self.distance = 0

    
    def distance_velocity(self, msg):
        # Get the desired x and y positions from the parameter server
        des_x = rospy.get_param('/des_pos_x')
        des_y = rospy.get_param('/des_pos_y')

        # Get the window size for the velocity calculation from the parameter server
        velocity_window_size = rospy.get_param('/window_size')
        
        # Get the actual x and y positions from the message
        x = msg.pos_x
        y = msg.pos_y
        des_coord = [des_x, des_y]
        coord = [x, y]
        self.distance = math.dist(des_coord, coord)
        # Calculating the average velocity
        if isinstance(msg.vel_x, list):
            vel_data = msg.vel_x[-velocity_window_size:]
        else:
            vel_data = [msg.vel_x]
            self.averagevelx = sum(vel_data) / min(len(vel_data), velocity_window_size)

    def values(self, _):      
        return Ave_pos_velResponse(self.distance, self.averagevelx)		      

    def spin(self):
        rospy.spin()

# Main function
if __name__ == "__main__":

    service = NodeThree()
    dist_vel_service = rospy.ServiceProxy('info_service', Ave_pos_vel)

    while not rospy.is_shutdown():
            response = dist_vel_service()
 
 

    # Start the node
    service.spin()
