import time
import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import adafruit_icm20x
import busio

#NOTE: X, Y and Z are used in a weird way. They're different for the IMU, the physical controller and the gamepad. Be Careful!

import usb_hid
from gamepad import Gamepad
gp = Gamepad(usb_hid.devices)

x_in_range = 0
y_in_range = 0


#buttons
button_pins = [board.GP20, board.GP12, board.GP13, board.GP18]
buttons = []
for pin in button_pins:
    button = DigitalInOut(pin)
    button.direction = Direction.INPUT
    button.pull = Pull.UP
    buttons.append(button)

z_in = AnalogIn(board.A2)

x_pins = [board.GP7, board.GP8,board.GP9, board.GP10, board.GP11]
x_leds = []
for pin in x_pins:
    led = DigitalInOut(pin)
    led.direction = Direction.OUTPUT
    led.value = False
    x_leds.append(led)
    
y_pins = [board.GP5, board.GP6, board.GP14, board.GP15]
y_leds = []
for pin in y_pins:
    led = DigitalInOut(pin)
    led.direction = Direction.OUTPUT
    led.value = False
    y_leds.append(led)
    
z_pins = [board.GP27, board.GP26, board.GP21, board.GP17, board.GP16]
z_leds = []
for pin in z_pins:
    led = DigitalInOut(pin)
    led.direction = Direction.OUTPUT
    led.value = False
    z_leds.append(led)
    
i2c = busio.I2C(board.GP1, board.GP0)  # uses board.SCL and board.SDA
icm = adafruit_icm20x.ICM20948(i2c)

while True:
    y_accel = icm.acceleration[1]
    x_accel = icm.acceleration[0]
    z_val = z_in.value
    print(z_in.value)
    for led in x_leds:
        led.value = False
        
    if(y_accel) > 4:
        x_leds[0].value = True
        x_in_range = 127
    elif(y_accel) > 2:
        x_leds[1].value = True
        x_in_range = 60
    elif(y_accel) < -4:
        x_leds[4].value = True
        x_in_range = -127
    elif(y_accel) < -2:
        x_leds[3].value = True
        x_in_range = -60
    else:
        x_leds[2].value = True
        x_in_range = 0
        
    for led in y_leds:
        led.value = False
    
    if(x_accel) < - 8:
        y_leds[0].value = True
    elif(x_accel) < -6:
        y_leds[1].value = True
    elif(x_accel) > -1:
        y_leds[3].value = True
    elif(x_accel) > -3:
        y_leds[2].value = True

    for led in z_leds:
        led.value = False
    
    if(z_val > 62000):
        z_leds[0].value = True
        y_in_range = 127
    elif(z_val > 45000):
        z_leds[1].value = True
        y_in_Range = 60
    elif(z_val > 28000):
        z_leds[2].value = True
        y_in_range = 0
    elif(z_val > 10500):
        z_leds[3].value = True
        y_in_range = -60
    else:
        z_leds[4].value = True
        y_in_range = -127
        
    gp.move_joysticks(x=-x_in_range, y=-y_in_range)
        
    for i in range(len(buttons)):
        if(not buttons[i].value) :
            gp.press_buttons(i+1)
        else:
            gp.release_buttons(i+1)
    
    time.sleep(0.05)
