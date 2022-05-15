print ("Tata is starting")

import board

from kmk.extensions.rgb import RGB, AnimationModes
from kmk.extensions.oled import OLED
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
from kmk.kmk_keyboard import KMKKeyboard
from kmk.handlers.sequences import simple_key_sequence as sks

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

keyboard.rgb_pixel_pin = board.GP4
keyboard.pixel_pin = board.GP4
keyboard.num_pixels = 9

rgb_ext = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=9,
              hue_default = 128, sat_default = 248, val_default = 16,
              hue_step = 8, sat_step = 8, val_step = 8,
              animation_speed = 4, breathe_center = 2, knight_effect_length = 4,
              animation_mode = AnimationModes.SWIRL)

keyboard.extensions.append(rgb_ext)

keyboard.col_pins = (board.GP8, board.GP7, board.GP9, board.GP10,)
keyboard.row_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

DEL_CHROME = sks((KC.LGUI(KC.K),))
CHROME = sks((KC.LGUI(KC.C),))
BLUETOOTH = sks((KC.LGUI(KC.B),))
LOGIN = sks((KC.N5, KC.N6, KC.N6, KC.N5,))
SHUTDOWN = sks((KC.LGUI(KC.LSFT(KC.S)),))
LAYER = KC.MO(1)

keyboard.keymap = [
    [
        KC.RGB_TOG, KC.ENT,            KC.ESC,              LAYER,
        DEL_CHROME, KC.RGB_ANI,        KC.RGB_AND,          KC.TRNS,
        CHROME,     KC.RGB_VAI,        KC.RGB_VAD,          KC.TRNS,
        BLUETOOTH,  KC.RGB_SAI,        KC.RGB_SAD,          KC.TRNS,
        LOGIN,      KC.RGB_HUI,        KC.RGB_HUD,          KC.TRNS
    ],
    [
        SHUTDOWN,            KC.TRNS,             KC.TRNS,                     KC.TRNS,
        KC.TRNS,             KC.TRNS,             KC.TRNS,                     KC.TRNS,
        KC.TRNS,             KC.TRNS,             KC.TRNS,                     KC.TRNS,
        KC.RGB_MODE_BREATHE, KC.RGB_MODE_RAINBOW, KC.RGB_MODE_BREATHE_RAINBOW, KC.TRNS,
        KC.RGB_MODE_PLAIN,   KC.RGB_MODE_KNIGHT,  KC.RGB_MODE_SWIRL,           KC.RESET
    ]
]

keyboard.debug_enabled = True

oled_text=['Log BT Chrome Del', 'Kolory', 'Prawy dol+gora=reset']

oled_ext = OLED(oled_text, 10)

keyboard.extensions.append(oled_ext)

def enable_usb_storage():
    print("Enabling usb storage on subsequent restart")
    import storage
    storage.remount("/", readonly=False)
    import os
    os.rename('boot.py', 'boot_old.py')

print("All loaded")

if __name__ == '__main__':
    keyboard.go()
