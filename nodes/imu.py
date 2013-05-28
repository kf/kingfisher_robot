#!/usr/bin/python

import roslib; roslib.load_manifest('kingfisher_nmea')
import rospy

from nmea_helpers import TxHelper
from sensor_msgs.msg import Imu

class RawIMU(TxHelper):
  SENTENCE = "IMU" 

  def __init__(self):
    rospy.Subscriber("imu/data", Imu, self._cb)

  def _cb(self, msg):
    self.tx(self.gps_time(msg.header.stamp),
        msg.angular_velocity.x,
        msg.angular_velocity.y,
        msg.angular_velocity.z,
        msg.linear_acceleration.x,
        msg.linear_acceleration.y,
        msg.linear_acceleration.z)

class RawCompass(TxHelper):
  SENTENCE = "RCM" 

  def __init__(self):
    rospy.Subscriber("imu/rpy", Vector3Stamped, self._cb)

  def _cb(self, msg):
    self.tx(self.gps_time(msg.header.stamp),
        msg.angular_velocity.x,
        msg.angular_velocity.y,
        msg.angular_velocity.z,
        msg.linear_acceleration.x,
        msg.linear_acceleration.y,
        msg.linear_acceleration.z)

if __name__ == "__main__":
  rospy.init_node('nmea_imu')
  #RawCompass()
  RawIMU()
  rospy.spin()
