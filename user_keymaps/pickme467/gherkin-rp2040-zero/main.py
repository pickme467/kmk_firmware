print ("Gherkin rp2040-zero is starting")

import board

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.tapdance import TapDance
from kmk.scanners import DiodeOrientation
from kmk.kmk_keyboard import KMKKeyboard
from kmk.handlers.sequences import send_string
keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())
keyboard.modules.append(TapDance())

from kmk.extensions.rgb import RGB, AnimationModes
keyboard.rgb_pixel_pin = board.GP5
keyboard.pixel_pin = board.GP5
keyboard.num_pixels = 8

rgb_ext = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=8,
              val_default=10, animation_mode = AnimationModes.SWIRL)

keyboard.extensions.append(rgb_ext)
rgb_ext._rgb_tog()

from kmk.extensions.solenoid import Solenoid
solenoid_ext = Solenoid(solenoid_pin = board.GP28, led_pin = None)
keyboard.extensions.append(solenoid_ext)

def read_secrets():
    s = []
    with open('secrets.txt', 'r') as f:
        s = f.readlines()
    return s

keyboard.col_pins = ( board.GP12,  board.GP11, board.GP10, board.GP9, board.GP26, board.GP14,)
keyboard.row_pins = ( board.GP1,  board.GP2,  board.GP3,  board.GP4,  board.GP6,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.coord_mapping = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
]

# Layers
BASE = 0
NUMBERS = 1
RALTS = 2
FUNCTIONS = 3
STRINGS = 4
MOD = 5

# Tap Dance
TD_UPPER_LOWER_MOD = KC.TD(
    KC.MO(NUMBERS),
    KC.MO(FUNCTIONS),
    KC.MO(STRINGS)
    )

FN_MOD = KC.MO(MOD)

# Keys
FNRA_A = KC.RALT(KC.A)
FNRA_C = KC.RALT(KC.C)
FNRA_E = KC.RALT(KC.E)
FNRA_L = KC.RALT(KC.L)
FNRA_N = KC.RALT(KC.N)
FNRA_O = KC.RALT(KC.O)
FNRA_S = KC.RALT(KC.S)
FNRA_X = KC.RALT(KC.X)
FNRA_Z = KC.RALT(KC.Z)
FN_AST = KC.LSFT(KC.N8)

FN_J = KC.MO(RALTS)
FN_X = TD_UPPER_LOWER_MOD

HYPER = KC.F9
SUPER = KC.F8

secrets = read_secrets()
MC_SU1 = send_string(secrets[0])
MC_ROOT = send_string(secrets[1])

XXXXXXX = KC.TRNS
RGB_TOG = KC.RGB_TOG

keyboard.keymap = [[
     FN_MOD,   KC.COMM,    KC.DOT,      KC.P,      KC.Y,      KC.F,      KC.G,      KC.C,      KC.R,      KC.L,
       KC.A,      KC.O,      KC.E,      KC.U,      KC.I,      KC.D,      KC.H,      KC.T,      KC.N,      KC.S,
    KC.SCLN,      KC.Q,      FN_J,      KC.K,      FN_X,    KC.SPC,      KC.M,      KC.W,      KC.V,      KC.Z,
], [
    KC.BSLS,   KC.COMM,    KC.DOT,   KC.PIPE,    FN_AST,   KC.QUES,     KC.N1,     KC.N2,     KC.N3,     KC.N0,
     KC.TAB,    KC.EQL,   KC.PLUS,   KC.UNDS,   KC.MINS,   KC.SLSH,     KC.N4,     KC.N5,     KC.N6,   KC.BSPC,
     KC.ESC,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,     KC.N7,     KC.N8,     KC.N9,    KC.ENT,
], [
  KC.INSERT,    KC.GRV,   KC.TILD,   KC.LBRC,   KC.LABK,   KC.RABK,   KC.RBRC,    FNRA_C,    XXXXXXX,    FNRA_L,
     FNRA_A,    FNRA_O,    FNRA_E,   KC.LPRN,   KC.LCBR,   KC.RCBR,   KC.RPRN,     KC.UP,     FNRA_N,    FNRA_S,
  KC.DELETE,     SUPER,   XXXXXXX,     HYPER,    FNRA_X,      KC.B,   KC.LEFT,   KC.DOWN,   KC.RIGHT,    FNRA_Z,
], [
    KC.LSFT,   KC.LCTL,   KC.LALT,   KC.LGUI,   XXXXXXX,   XXXXXXX,   KC.RGUI,   KC.LALT,   KC.RCTL,   KC.RSFT,
    KC.CLCK,   KC.SLCK,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   KC.PGUP,   XXXXXXX,   RGB_TOG,
   KC.RESET,   XXXXXXX,   XXXXXXX,      KC.X,   XXXXXXX,   XXXXXXX,   KC.HOME, KC.PGDOWN,    KC.END,    KC.ENT,
], [
      KC.F1,     KC.F2,     KC.F3,     KC.F4,     KC.F5,     KC.F6,     KC.F7,     KC.F8,     KC.F9,    KC.F10,
    XXXXXXX,   XXXXXXX,   KC.VOLU,   KC.MUTE,    KC.F11,    KC.F12,    MC_SU1,   XXXXXXX,   XXXXXXX,   XXXXXXX,
    XXXXXXX,   XXXXXXX,   KC.VOLD,   XXXXXXX,   XXXXXXX,   XXXXXXX,   MC_ROOT,   XXXXXXX,   XXXXXXX,   XXXXXXX,
], [
    XXXXXXX,   KC.LCTL,   KC.LALT,   KC.LGUI,   XXXXXXX,   XXXXXXX,   KC.RGUI,   KC.LALT,   KC.RCTL,   KC.RSFT,
    XXXXXXX,   XXXXXXX,   XXXXXXX,   KC.QUOT,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,
    XXXXXXX,   XXXXXXX,      KC.J,   XXXXXXX,      KC.X,      KC.B,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,
]]

keyboard.debug_enabled = True

print("All loaded")

def enable_usb_storage():
    print("Enabling usb storage on subsequent restart")
    import storage
    storage.remount("/", readonly=False)
    import os
    os.rename('boot.py', 'boot_old.py')

if __name__ == '__main__':
    keyboard.go()
