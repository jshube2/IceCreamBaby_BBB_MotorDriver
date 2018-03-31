import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

class Motor:
	def __init__(self, pin1, pin2, pwm, stby, default_speed=50):
		self.pin1 = pin1
		self.pin2 = pin2
		self.pwm  = pwm
		self.stby = stby
		self.default_speed = default_speed
		
		GPIO.setup(self.pin1, GPIO.OUT)
		GPIO.setup(self.pin2, GPIO.OUT)
		GPIO.setup(self.stby, GPIO.OUT)
		PWM.start(self.pwm, 0)
		
		GPIO.output(self.stby, GPIO.HIGH)
		return
	
	def setState(self, sgn, speed):
		self.setSpeed(speed)
		self.setDirection(sgn)
		return
	
	def setSpeed(self, speed=None):
		if speed is None:
			speed = self.default_speed

		PWM.start(self.pwm, speed)
		return
	
	def setDirection(self, sgn=1):
		if sgn == -1:
			GPIO.output(self.pin1, GPIO.LOW)
			GPIO.output(self.pin2, GPIO.HIGH)
		elif sgn == 1:
			GPIO.output(self.pin1, GPIO.HIGH)
			GPIO.output(self.pin2, GPIO.LOW)
		return
	
	def enable(self):
		GPIO.output(self.stby, GPIO.HIGH)
		PWM.start(self.pwm, self.default_speed)
		return
	
	def disable(self):
		GPIO.output(self.stby, GPIO.LOW)
		PWM.start(self.pwm, 0)
		return
	

		
	
