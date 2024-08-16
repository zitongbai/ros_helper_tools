#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Imu

from viz_attitude import VizAttitude

def imu_cb(msg):
    viz.update_from_quaternion([msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w])

if __name__ == '__main__':
    
    rospy.init_node('viz_imu_node')
    
    viz = VizAttitude()
    
    imu_topic = "/mujoco/imu"
    rospy.Subscriber(imu_topic, Imu, imu_cb)
    
    rospy.spin()