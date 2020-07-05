import RPi.GPIO as GPIO
import time
from getch import Getch 


# rfpin -> right wheel forward  rbpin -> right wheel backward
# lfpin -> left wheel forward  lbpin -> left wheel backward
# speed -> PWM freqency  accel -> acceleration
class Motor:
    def __init__(self, rfpin, rbpin, lfpin, lbpin, speed = 50, accel = 10):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.rfpin = rfpin # forward
        self.rbpin = rbpin # backword
        self.lfpin = lfpin # forward
        self.lbpin = lbpin # backword
        self.speed = speed
        self.accel = accel
        GPIO.setup(self.rfpin, GPIO.OUT)
        GPIO.setup(self.rbpin, GPIO.OUT)
        GPIO.setup(self.lfpin, GPIO.OUT)
        GPIO.setup(self.lbpin, GPIO.OUT)
        self.rforward = GPIO.PWM(self.rfpin, speed)
        self.rbackward = GPIO.PWM(self.rbpin, speed)
        self.lforward = GPIO.PWM(self.lfpin, speed)
        self.lbackward = GPIO.PWM(self.lbpin, speed)
        self.rforward.start(0)
        self.rbackward.start(0)
        self.lforward.start(0)
        self.lbackward.start(0)
        self.w_count = 0 # count of w press
        self.s_count = 0 # cuunt of s press
        self.d_count = 0
        self.a_count = 0
        self.max_count = (100 - speed) / accel
            
    def w_direction(self):
        self.s_count = 0
        self.d_count = 0
        self.a_count = 0
        self.rbackward.ChangeDutyCycle(0)
        self.lbackward.ChangeDutyCycle(0)
        if self.w_count < self.max_count:
            self.w_count += 1
            self.rforward.ChangeDutyCycle(self.speed + self.w_count * self.accel)
            self.lforward.ChangeDutyCycle(self.speed + self.w_count * self.accel)
        else:
            self.rforward.ChangeDutyCycle(100)
            self.lforward.ChangeDutyCycle(100)

    def s_direction(self):
        self.w_count = 0
        self.d_count = 0
        self.a_count = 0
        self.rforward.ChangeDutyCycle(0)
        self.lforward.ChangeDutyCycle(0)
        if self.s_count < self.max_count:
            self.s_count += 1
            self.rbackward.ChangeDutyCycle(self.speed + self.s_count * self.accel)
            self.lbackward.ChangeDutyCycle(self.speed + self.s_count * self.accel)
        else:
            self.rbackward.ChangeDutyCycle(100)
            self.lbackward.ChangeDutyCycle(100)

    def rturn(self):
        self.w_count = 0
        self.s_count = 0
        self.a_count = 0
        self.rbackward.ChangeDutyCycle(0)
        self.lbackward.ChangeDutyCycle(0)
        self.rforward.ChangeDutyCycle(50)
        if self.d_count < 3:
            self.d_count += 1
            self.lforward.ChangeDutyCycle(50 + self.d_count * 10)
        else:
            self.lforward.ChangeDutyCycle(50 + self.d_count * 10)
        
    def lturn(self):
        self.w_count = 0
        self.s_count = 0
        self.d_count = 0
        self.rbackward.ChangeDutyCycle(0)
        self.lbackward.ChangeDutyCycle(0)
        self.lforward.ChangeDutyCycle(50)
        if self.a_count < 3:
            self.a_count += 1
            self.rforward.ChangeDutyCycle(50 + self.a_count * 10)
        else:
            self.rforward.ChangeDutyCycle(50 + self.a_count * 10)
            
    def rcircle(self):
        self.rforward.ChangeDutyCycle(0)
        self.rbackward.ChangeDutyCycle(60)
        self.lbackward.ChangeDutyCycle(0)
        self.lforward.ChangeDutyCycle(60)

    def lcircle(self):
        self.rbackward.ChangeDutyCycle(0)
        self.rforward.ChangeDutyCycle(60)
        self.lforward.ChangeDutyCycle(0)
        self.lbackward.ChangeDutyCycle(60)
    
    def breaking(self):
        self.w_count = 0
        self.s_count = 0
        self.rforward.ChangeDutyCycle(0)
        self.rbackward.ChangeDutyCycle(0)
        self.lforward.ChangeDutyCycle(0)
        self.lbackward.ChangeDutyCycle(0)

    def parking(self):
        self.w_count = 0
        self.s_count = 0
        self.rforward.ChangeDutyCycle(0)
        self.rbackward.ChangeDutyCycle(0)
        self.lforward.ChangeDutyCycle(0)
        self.lbackward.ChangeDutyCycle(0)
        GPIO.cleanup()
        
