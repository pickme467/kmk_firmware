print ("Tata is starting")

import board

from kmk.extensions.rgb import RGB, AnimationModes
from kmk.keys import KC
# from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
from kmk.kmk_keyboard import KMKKeyboard

keyboard = KMKKeyboard()

# keyboard.modules.append(Layers())

keyboard.rgb_pixel_pin = board.GP4
keyboard.pixel_pin = board.GP4
keyboard.num_pixels = 9

rgb_ext = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=9,
              hue_default = 127, sat_default = 255, val_default = 64,
              hue_step = 10, sat_step = 10, val_step = 10,
              animation_speed = 5, breathe_center = 2, knight_effect_length = 5,
              animation_mode = AnimationModes.SWIRL)

keyboard.extensions.append(rgb_ext)

keyboard.col_pins = (board.GP8, board.GP7, board.GP9, board.GP10,)
keyboard.row_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.RGB_TOG, KC.RGB_MODE_PLAIN, KC.RGB_MODE_BREATHE,         KC.RGB_MODE_RAINBOW,
        KC.RGB_HUI, KC.RGB_VAI,        KC.RGB_MODE_BREATHE_RAINBOW, KC.Q,
        KC.RGB_HUD, KC.RGB_VAD,        KC.RGB_MODE_KNIGHT,          KC.TRNS,
        KC.RGB_SAI, KC.RGB_ANI,        KC.RGB_MODE_SWIRL,           KC.TRNS,
        KC.RGB_SAD, KC.RGB_AND,        KC.O,                        KC.T,
    ]
]

keyboard.debug_enabled = True

# OLED
import busio
import board
import adafruit_ssd1306

i2c = busio.I2C(board.GP27, board.GP26)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
oled.text('YamPAD + KMK', 0, 10, 1)
oled.show()


def enable_usb_storage():
    print("Enabling usb storage on subsequent restart")
    import storage
    storage.remount("/", readonly=False)
    import os
    os.rename('boot.py', 'boot_old.py')


if __name__ == '__main__':
    keyboard.go()
