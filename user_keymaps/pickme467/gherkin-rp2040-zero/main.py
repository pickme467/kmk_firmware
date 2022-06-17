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

# Tap Dance
TD_UPPER_LOWER_MOD = KC.TD(
    KC.MO(NUMBERS),
    KC.MO(FUNCTIONS),
    KC.MO(STRINGS)
    )

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

TAPPING_TERM = 157
SHIFT_TAPPING_TERM = 177
ALT_TAPPING_TERM = 177
GUI_TAPPING_TERM = 177
CTRL_TAPPING_TERM = 177

FN_P = KC.MT(KC.P, KC.LGUI, prefer_hold=False, tap_interrupted=False, tap_time=GUI_TAPPING_TERM)
FN_G = KC.MT(KC.G, KC.RGUI, prefer_hold=True, tap_interrupted=True, tap_time=GUI_TAPPING_TERM)

FN_DOT = KC.MT(KC.DOT, KC.LALT, prefer_hold=True, tap_interrupted=True, tap_time=ALT_TAPPING_TERM)
FN_C = KC.MT(KC.C, KC.LALT, prefer_hold=True, tap_interrupted=True, tap_time=ALT_TAPPING_TERM)

FN_COMM = KC.MT(KC.COMM, KC.LCTL, prefer_hold=True, tap_interrupted=True, tap_time=CTRL_TAPPING_TERM)
FN_R = KC.MT(KC.R, KC.RCTL, prefer_hold=False, tap_interrupted=False, tap_time=CTRL_TAPPING_TERM)

FN_L = KC.MT(KC.L, KC.RSFT, prefer_hold=True, tap_interrupted=True, tap_time=SHIFT_TAPPING_TERM)
FN_QUOT = KC.MT(KC.QUOT, KC.LSFT, prefer_hold=True, tap_interrupted=True, tap_time=SHIFT_TAPPING_TERM)

FN_J = KC.LT(RALTS, KC.J, prefer_hold=True, tap_interrupted=False, tap_time=TAPPING_TERM)

FN_X = TD_UPPER_LOWER_MOD

HYPER = KC.F9
SUPER = KC.F8

secrets = read_secrets()
MC_SU1 = send_string(secrets[0])
MC_ROOT = send_string(secrets[1])

RESET = KC.RESET
XXXXXXX = KC.TRNS
RGB_TOG = KC.RGB_TOG

KC_F1 = KC.F1
KC_F2 = KC.F2
KC_F3 = KC.F3
KC_F4 = KC.F4
KC_F5 = KC.F5
KC_F6 = KC.F6
KC_F7 = KC.F7
KC_F8 = KC.F8
KC_F9 = KC.F9
KC_F10 = KC.F10
KC_F11 = KC.F11
KC_F12 = KC.F12

KC_0 = KC.N0
KC_1 = KC.N1
KC_2 = KC.N2
KC_3 = KC.N3
KC_4 = KC.N4
KC_5 = KC.N5
KC_6 = KC.N6
KC_7 = KC.N7
KC_8 = KC.N8
KC_9 = KC.N9

KC_A = KC.A
KC_B = KC.B
KC_D = KC.D
KC_E = KC.E
KC_F = KC.F
KC_H = KC.H
KC_I = KC.I
KC_K = KC.K
KC_M = KC.M
KC_N = KC.N
KC_O = KC.O
KC_Q = KC.Q
KC_S = KC.S
KC_T = KC.T
KC_U = KC.U
KC_V = KC.V
KC_W = KC.W
KC_X = KC.X
KC_Y = KC.Y
KC_Z = KC.Z

KC_BSLS = KC.BSLS
KC_BSPC = KC.BSPC
KC_INSERT = KC.INSERT
KC_DELETE = KC.DELETE

KC_CLCK = KC.CLCK

KC_COMM = KC.COMM
KC_DOT = KC.DOT
KC_PLUS = KC.PLUS
KC_MINS = KC.MINS
KC_EQL = KC.EQL
KC_PIPE = KC.PIPE
KC_QUES = KC.QUES
KC_SLSH = KC.SLSH
KC_TILD = KC.TILD
KC_UNDS = KC.UNDS

KC_ENT = KC.ENT
KC_ESC = KC.ESC
KC_SPC = KC.SPC
KC_TAB = KC.TAB

KC_GRV = KC.GRV

KC_HOME = KC.HOME
KC_END = KC.END
KC_PGDOWN = KC.PGDOWN
KC_PGUP = KC.PGUP
KC_UP = KC.UP
KC_DOWN = KC.DOWN
KC_LEFT = KC.LEFT
KC_RIGHT = KC.RIGHT

KC_LBRC = KC.LBRC
KC_RBRC = KC.RBRC
KC_LCBR = KC.LCBR
KC_RCBR = KC.RCBR
KC_LPRN = KC.LPRN
KC_RPRN = KC.RPRN

KC_GT = KC.RABK
KC_LT = KC.LABK

KC_SCLN = KC.SCLN
KC_SLCK = KC.SLCK

KC_VOLD = KC.VOLD
KC_VOLU = KC.VOLU
KC_MUTE = KC.MUTE

keyboard.keymap = [[
    FN_QUOT,   FN_COMM,    FN_DOT,      FN_P,      KC_Y,      KC_F,      FN_G,      FN_C,      FN_R,      FN_L,
       KC_A,      KC_O,      KC_E,      KC_U,      KC_I,      KC_D,      KC_H,      KC_T,      KC_N,      KC_S,
    KC_SCLN,      KC_Q,      FN_J,      KC_K,      FN_X,    KC_SPC,      KC_M,      KC_W,      KC_V,      KC_Z,
], [
    KC_BSLS,   KC_COMM,    KC_DOT,   KC_PIPE,    FN_AST,   KC_QUES,      KC_1,      KC_2,      KC_3,      KC_0,
     KC_TAB,    KC_EQL,   KC_PLUS,   KC_UNDS,   KC_MINS,   KC_SLSH,      KC_4,      KC_5,      KC_6,   KC_BSPC,
     KC_ESC,   XXXXXXX,   XXXXXXX,      KC_X,   XXXXXXX,      KC_B,      KC_7,      KC_8,      KC_9,    KC_ENT,
], [
  KC_INSERT,    KC_GRV,   KC_TILD,   KC_LBRC,     KC_LT,     KC_GT,   KC_RBRC,    FNRA_C,    XXXXXXX,    FNRA_L,
     FNRA_A,    FNRA_O,    FNRA_E,   KC_LPRN,   KC_LCBR,   KC_RCBR,   KC_RPRN,     KC_UP,     FNRA_N,    FNRA_S,
  KC_DELETE,     SUPER,   XXXXXXX,     HYPER,    FNRA_X,      KC_B,   KC_LEFT,   KC_DOWN,   KC_RIGHT,    FNRA_Z,
], [
    XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,
    KC_CLCK,   KC_SLCK,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   KC_PGUP,   XXXXXXX,   RGB_TOG,
      RESET,   XXXXXXX,   XXXXXXX,      KC_X,   XXXXXXX,   XXXXXXX,   KC_HOME, KC_PGDOWN,    KC_END,    KC_ENT,
], [
      KC_F1,     KC_F2,     KC_F3,     KC_F4,     KC_F5,     KC_F6,     KC_F7,     KC_F8,     KC_F9,    KC_F10,
    XXXXXXX,   XXXXXXX,   KC_VOLU,   KC_MUTE,    KC_F11,    KC_F12,    MC_SU1,   XXXXXXX,   XXXXXXX,   XXXXXXX,
    XXXXXXX,   XXXXXXX,   KC_VOLD,   XXXXXXX,   XXXXXXX,   XXXXXXX,   MC_ROOT,   XXXXXXX,   XXXXXXX,   XXXXXXX,
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
