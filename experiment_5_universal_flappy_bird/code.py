import time
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull
from board import *

import usb_hid
from gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

button_x = DigitalInOut(GP17)
button_x.direction = Direction.INPUT
button_x.pull = Pull.UP

button_y = DigitalInOut(GP21)
button_y.direction = Direction.INPUT
button_y.pull = Pull.UP

button_1 = DigitalInOut(GP9)
button_1.direction = Direction.INPUT
button_1.pull = Pull.UP

button_2 = DigitalInOut(GP13)
button_2.direction = Direction.INPUT
button_2.pull = Pull.UP

speed_x = -127
speed_y = -127

jump = 60
jump_back = 3

counter_x = 0
limit_x = 1
pressed_x = False

counter_y = 0
limit_y = 1
pressed_y = False

while True:
    if (not button_x.value):
        if (not pressed_x):
            speed_x = speed_x + jump
            if speed_x > 127:
                speed_x = 127
        pressed_x = True

    if (button_x.value or pressed_x):
        if (button_x.value):
            pressed_x = False
        counter_x = counter_x + 1
        if counter_x > limit_x:
            speed_x = speed_x-jump_back
            if speed_x < -127:
                speed_x = -127

    if (not button_y.value):
        if (not pressed_y):
            speed_y = speed_y + jump
            if speed_y > 127:
                speed_y = 127
        pressed_y = True

    if (button_y.value or pressed_y):
        if (button_y.value):
            pressed_y = False
        counter_y = counter_y + 1
        if counter_y > limit_y:
            speed_y = speed_y-jump_back
            if speed_y < -127:
                speed_y = -127

    gp.move_joysticks(x=speed_x, y=speed_y)

    if(not button_1.value):
        gp.press_buttons(1)
    else:
        gp.release_buttons(1)

    if(not button_2.value):
        gp.press_buttons(2)
    else:
        gp.release_buttons(2)

    print(speed_x, speed_y)


    time.sleep(0.01)