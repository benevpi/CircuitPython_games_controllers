import time
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull
import touchio
from board import *

import usb_hid
from gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

slider_x = AnalogIn(board.A1)
slider_y = AnalogIn(board.A2)

#want to tweak the values so it's easier to get gentle turns
'''
def get_range(pin):
    return int((pin.value - 32768) / (256*2))*2
'''
def get_range(pin):
    if pin.value < 32768:
        multiplier = -1
    else:
        multiplier = 1
    return int(((pin.value - 32768) / (2895))**2) * multiplier

num_buttons = 3
touch_pins = [GP9, GP8, GP20, GP19]
touch_inputs = []
for pin in touch_pins:
    touch_inputs.append(touchio.TouchIn(pin))

button_pins = [GP16, GP2, GP21]
button_inputs = []
for button in button_pins:
    button_in = DigitalInOut(button)
    button_in.direction = Direction.INPUT
    button_in.pull = Pull.UP
    button_inputs.append(button_in)

while True:
    print(get_range(slider_x))
    print(touch_inputs[0].raw_value)

    gp.move_joysticks(x=get_range(slider_x), y=-get_range(slider_y))

    for i in range(len(button_inputs)):
        if(not button_inputs[i].value) :
            gp.press_buttons(i+1)
        else:
            gp.release_buttons(i+1)
    for i in range(len(touch_inputs)):
        if (touch_inputs[i].value):
            gp.press_buttons(i+1+num_buttons)
        else:
            gp.release_buttons(i+1+num_buttons)

    time.sleep(0.1)