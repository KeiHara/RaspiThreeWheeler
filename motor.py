import RPi.GPIO as GPIO
import time
import curses

class Motor:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.fpin = 16 # forward
        self.bpin = 18 # backword
        GPIO.setup(self.fpin, GPIO.OUT)
        GPIO.setup(self.bpin, GPIO.OUT)
        self.forward = GPIO.PWM(self.fpin, 50)
        self.backward = GPIO.PWM(self.bpin, 50)
        self.forward.start(0)
        self.backward.start(0)
    
    def MotorDrive(self):
        count = 0
        while True:
            if count == 10:
                self.forward.stop()
                self.backward.stop()
                break
            else:
                self.forward.ChangeDutyCycle(50)
                self.backward.ChangeDutyCycle(0)
                time.sleep(3)
                self.forward.ChangeDutyCycle(0)
                self.backward.ChangeDutyCycle(50)
                time.sleep(3)
                count += 1

	
motor = Motor()
motor.MotorDrive()
GPIO.cleanup()
