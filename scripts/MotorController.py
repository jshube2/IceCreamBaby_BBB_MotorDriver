#!/usr/bin/python
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

import rospy
from geometry_msgs.msg import Twist

from Motor import Motor

class MotorController:
	def __init__(self):
		self.max_speed = 50
		self.backLeftMotor = Motor("P8_11", "P8_12", "P8_13", "P8_14")
		self.frontLeftMotor = Motor("P8_17", "P8_15", "P8_19", "P8_14")
		self.backRightMotor = Motor("P9_11", "P9_12", "P9_14", "P9_17")
		self.frontRightMotor = Motor("P9_13", "P9_15", "P9_16", "P9_17")
		return
		
	def run(self):
		rospy.Subscriber('/rover/cmd', Twist, self.ctrlCallback)
		rospy.spin()
		
		self.shutdown()
		return
	
	def ctrlCallback(self, twist_msg):
		# lx = 16.5cm -> 0.165m
		# ly = 12.0cm -> 0.120m
		lx = 0.165
		ly = 0.120
		scale = 2.0 + lx + ly
		
		vx = -twist_msg.linear.y
		vy = twist_msg.linear.x
		vz = twist_msg.linear.z
		wx = twist_msg.angular.x
		wy = twist_msg.angular.y
		wz = 4*twist_msg.angular.z

		w1 = (vx - vy - (lx + ly)*wz) / scale * self.max_speed
		w2 = (vx + vy + (lx + ly)*wz) / scale * self.max_speed
		w3 = (vx + vy - (lx + ly)*wz) / scale * self.max_speed
		w4 = (vx - vy + (lx + ly)*wz) / scale * self.max_speed
		print w1, w2, w3, w4
		self.frontLeftMotor.setState(self.sign(w1), abs(w1))
		self.frontRightMotor.setState(self.sign(w2), abs(w2))
		self.backLeftMotor.setState(self.sign(w3), abs(w3))
		self.backRightMotor.setState(self.sign(w4), abs(w4))

		return
	
	def stopAllMotors(self):
		self.backLeftMotor.setState(1, 0)
		self.frontLeftMotor.setState(1, 0)
		self.backRightMotor.setState(1, 0)
		self.frontRightMotor.setState(1, 0)
		return
	
	def enableAllMtors(self):
		self.backLeftMotor.enable()
		self.frontLeftMotor.enable()
		self.backRightMotor.enable()
		self.frontRightMotor.enable()
		return
	
	def disableAllMotors(self):
		self.backLeftMotor.disable()
		self.frontLeftMotor.disable()
		self.backRightMotor.disable()
		self.frontRightMotor.disable()
		return
		
	def shutdown(self):
		self.stopAllMotors()
		self.backLeftMotor.disable()
		self.frontLeftMotor.disable()
		self.backRightMotor.disable()
		self.frontRightMotor.disable()
		PWM.cleanup()
		GPIO.cleanup()
		return

	def sign(self, w):
		if w == 0:
			return 1
		else:
			return int(w / abs(w))

	
if __name__ == "__main__":
	rospy.init_node('Motor_Controller_Node')
	rospy.loginfo("Initializing Motor Controller\n")
	mc = MotorController()
	mc.run()
	rospy.loginfo("Closing Motor Controller\n")	
		
	
