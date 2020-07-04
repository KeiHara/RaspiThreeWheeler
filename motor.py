import RPi.GPIO as GPIO
import time
import curses

class Motor:
	def __init__(self):
		GPIO.cleanp()
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(16, GPIO.OUT)
		GPIO.setup(18, GPIO.OUT)

def MotorDrive( iIn1Pin, iIn2Pin, motor ):
	if 5 > motor and -5 < motor:
		GPIO.pwmWrite( iIn1Pin, 0.0 )
		GPIO.pwmWrite( iIn2Pin, 0.0 )
	elif 0 < motor:
		GPIO.pwmWrite( iIn1Pin, motor * 0.01 )
		GPIO.pwmWrite( iIn2Pin, 0.0 )
	else:
		GPIO.pwmWrite( iIn1Pin, 0.0 )
		GPIO.pwmWrite( iIn2Pin, -motor * 0.01 )

IN1PIN = 23
IN2PIN = 24

GPIO.setFunction( IN1PIN, GPIO.PWM )
GPIO.setFunction( IN2PIN, GPIO.PWM )

motor = 0
increase = 10

while 1:
	MotorDrive( IN1PIN, IN2PIN, motor )
	motor += increase
	if 100 < motor:
		motor = 90
		increase = -10
	if -100 > motor:
		motor = -90
		increase = 10
	webiopi.sleep( 1.0 )
