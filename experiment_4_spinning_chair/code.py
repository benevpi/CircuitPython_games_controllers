import time
import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import adafruit_icm20x
import busio
import math
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

x_min = -12
x_max = 40

y_min = -5
y_max = 40

#stolen from https://learn.adafruit.com/circuit-playground-express-compass/circuitpython
def normalize(value, in_min, in_max):
    mapped = (value - in_min) * 200 / (in_max - in_min) + -100
    return max(min(mapped, 100), -100)

i2c = busio.I2C(board.GP1, board.GP0)  # uses board.SCL and board.SDA
icm = adafruit_icm20x.ICM20948(i2c)

#buttons
button_pins = [board.GP20, board.GP12, board.GP13, board.GP18]
buttons = []
for pin in button_pins:
    button = DigitalInOut(pin)
    button.direction = Direction.INPUT
    button.pull = Pull.UP
    buttons.append(button)

z_in = AnalogIn(board.A2)

z_pins = [board.GP27, board.GP26, board.GP21, board.GP17, board.GP16]
z_leds = []
for pin in z_pins:
    led = DigitalInOut(pin)
    led.direction = Direction.OUTPUT
    led.value = False
    z_leds.append(led)

def get_degree():
    value = icm.gyro[2]
    if (value < 0):
        return math.ceil(value)
    if (value >= 0):
        return math.floor(value)

direction = 0
last_direction = 0
last_spin = 0
while True:
    z_val = z_in.value
    spin = get_degree()

    if spin < 0:
        #turn right
        if last_spin < 0:
            pass
            #continue spinning
        else:
            #start spinning
            keyboard.press(Keycode.RIGHT_ARROW)
            keyboard.release(Keycode.LEFT_ARROW)

    if spin > 0:
        #turn left
        if last_spin > 0:
            pass
            #continue spinning
        else:
            #start spinning
            keyboard.press(Keycode.LEFT_ARROW)
            keyboard.release(Keycode.RIGHT_ARROW)
    if spin == 0:
        keyboard.release(Keycode.LEFT_ARROW)
        keyboard.release(Keycode.RIGHT_ARROW)

    for led in z_leds:
        led.value = False

    if(z_val > 62000):
        z_leds[0].value = True
        keyboard.press(Keycode.UP_ARROW)
        keyboard.release(Keycode.DOWN_ARROW)
    elif(z_val > 45000):
        z_leds[1].value = True
        keyboard.press(Keycode.UP_ARROW)
        keyboard.release(Keycode.DOWN_ARROW)
    elif(z_val > 28000):
        z_leds[2].value = True
        keyboard.release(Keycode.UP_ARROW)
        keyboard.release(Keycode.DOWN_ARROW)
    elif(z_val > 10500):
        z_leds[3].value = True
        keyboard.release(Keycode.UP_ARROW)
        keyboard.press(Keycode.DOWN_ARROW)
    else:
        z_leds[4].value = True
        keyboard.release(Keycode.UP_ARROW)
        keyboard.press(Keycode.DOWN_ARROW)

    if buttons[2].value == False:
        keyboard.press(Keycode.ENTER)
        print("enter")
    else:
        keyboard.release(Keycode.ENTER)

    time.sleep(0.05)