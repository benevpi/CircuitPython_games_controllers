import rotaryio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull
import time

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

button = DigitalInOut(board.GP21)
button.direction = Direction.INPUT
button.pull = Pull.UP

encoder = rotaryio.IncrementalEncoder(board.GP11, board.GP10)
last_position = 0

last_button = False

def pause():
    for i in range(20000):
        pass

while True:
    position = encoder.position
    if last_position is None or position != last_position:
        print(position)
        if (last_position > position):
                keyboard.press(Keycode.Z)

                keyboard.release(Keycode.X)
        else:
            keyboard.press(Keycode.X)
            keyboard.release(Keycode.Z)

    if (last_position == position):
        keyboard.release(Keycode.Z)
        keyboard.release(Keycode.X)

    last_position = position

    if (not last_button and not button.value):
        keyboard.press(Keycode.Q)
        pause()
        last_button = True

    if (button.value):
        last_button = False
        keyboard.release(Keycode.Q)
    time.sleep(0.01)

