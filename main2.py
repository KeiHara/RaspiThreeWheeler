import time
from getch import Getch
from twin_motor import Motor

motor = Motor(16, 18, 40, 38)
while True:
    key = getch = Getch().getch()
    if key == 'w':
        motor.w_direction()
    elif key == 's':
        motor.s_direction()
    elif key == 'd':
        motor.rturn()
    elif key == 'a':
        motor.lturn()
    elif key == 'e':
        motor.rcircle()
    elif key == 'q':
        motor.lcircle()
    elif key == 'b':
        motor.breaking()
    elif key == 'p':
        motor.parking
        break

print('-- FINISH --')
