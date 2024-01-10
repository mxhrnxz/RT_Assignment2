#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
import actionlib
import actionlib.msg
from actionlib_msgs.msg import GoalStatus
from assignment_2_2023.msg import dataa, PlanningAction, PlanningGoal, PlanningResult


class NodeOne:
    def __init__(self):
        self.pub = rospy.Publisher("/position_velocity", dataa, queue_size=1)
        self.sub = rospy.Subscriber("/odom", Odometry, self.pub_position_velocity)
        self.client = actionlib.SimpleActionClient('/reaching_goal', PlanningAction)
        self.client.wait_for_server()

    def user_commands(self):
        
        
        while not rospy.is_shutdown():
            command = input("To set a new goal press 'y'  or 'c' to cancel the current goal: ")
            goal = PlanningGoal()

            if command == 'y':
            
                input_x = float(input("Enter the new x position : "))
                input_y = float(input("Enter the new y position : "))
                rospy.set_param('/des_pos_x', input_x)
                rospy.set_param('/des_pos_y', input_y)
                goal.target_pose.pose.position.x = input_x
                goal.target_pose.pose.position.y = input_y
                self.client.send_goal(goal)
                rospy.loginfo("Last goal which was recieved: target_x = %f, target_y = %f", goal.target_pose.pose.position.x, goal.target_pose.pose.position.y)
            elif command == 'c':
                    self.client.cancel_goal()
                    rospy.loginfo("The goal has been cancelled")
            else:
                rospy.logwarn("Invalid command. Please only enter 'y' or 'c'.")

            

  
        
    def pub_position_velocity(self, msg):
    
        # Putting the data from odom subscriber to the pulisher
        pos_and_vel_data = dataa()
        pos_and_vel_data.pos_x = msg.pose.pose.position.x
        pos_and_vel_data.pos_y = msg.pose.pose.position.y
        pos_and_vel_data.vel_x = msg.twist.twist.linear.x
        pos_and_vel_data.vel_z = msg.twist.twist.angular.z
        # Publishing the message
        self.pub.publish(pos_and_vel_data)


def main():
    rospy.init_node('set_for_client')
    handler = NodeOne()
    handler.user_commands()

if __name__ == '__main__':
    main()

