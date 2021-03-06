#!/usr/bin/env python

import rospy
import actionlib
from rtcrobot_actions.msg import DockAction, DockGoal

if __name__ == "__main__":
    rospy.init_node("dock_script")
    ACTION_NAME = "/dock"
    rospy.loginfo("Connecting to %s..." % ACTION_NAME)
    client = actionlib.SimpleActionClient(ACTION_NAME, DockAction)
    client.wait_for_server()
    rospy.loginfo("Sending dock goal...")
    goal = DockGoal()
    client.send_goal(goal)
    rospy.loginfo("Done, press Ctrl-C to exit")
    rospy.spin()
