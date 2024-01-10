#!/usr/bin/env python3

import rospy
from assignment_2_2023.srv import Input, InputResponse
# Initialize the ROS service
def setup_input_service():
    rospy.Service('input', Input, handle_input_request)
    rospy.loginfo("The 'input' service is ready.")
    
# Retrieve the last target positions from parameters
def get_last_target_positions():
    last_target_pos_x = rospy.get_param('/des_pos_x', default=0)
    last_target_pos_y = rospy.get_param('/des_pos_y', default=0)
    return last_target_pos_x, last_target_pos_y

# Create and return the service response message
def generate_response(last_target_pos_x, last_target_pos_y):
    response = InputResponse()
    response.inputx = last_target_pos_x
    response.inputy = last_target_pos_y
    return response

# Handle incoming service requests
def handle_input_request(_):
    last_target_pos_x, last_target_pos_y = get_last_target_positions()
    return generate_response(last_target_pos_x, last_target_pos_y)

# Main function
def start_last_target_service():
    rospy.init_node('last_target_service')
    setup_input_service()
    rospy.spin()

if __name__ == "__main__":
    start_last_target_service()

