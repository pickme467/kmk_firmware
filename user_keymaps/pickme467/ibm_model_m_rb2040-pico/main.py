print ("IBM Model M is starting")

import board

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
from kmk.kmk_keyboard import KMKKeyboard
from kmk.handlers.sequences import simple_key_sequence as sks
from kmk.extensions.rgb import RGB, AnimationModes

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

keyboard.rgb_pixel_pin = board.GP26
keyboard.pixel_pin = board.GP26
keyboard.num_pixels = 8

rgb_ext = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=8,
              hue_default = 128, sat_default = 248, val_default = 16,
              hue_step = 8, sat_step = 8, val_step = 8,
              animation_speed = 4, breathe_center = 2, knight_effect_length = 4,
              animation_mode = AnimationModes.SWIRL)

keyboard.extensions.append(rgb_ext)

# from kmk.extensions.solenoid import Solenoid
# solenoid_ext = Solenoid(solenoid_pin = board.GP26, led_pin = board.LED)
# keyboard.extensions.append(solenoid_ext)

keyboard.col_pins = ( board.GP8,  board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15,
                      board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP28,)
keyboard.row_pins = ( board.GP0,  board.GP1,  board.GP2,  board.GP3,  board.GP4,  board.GP5,  board.GP6,  board.GP7,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

coord_mapping = [
#--|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
    125,  92,  91, 107, 123, 121, 119, 102,  86,  89,  73,  68,  67,  64,  48,  17,
#--|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
     93,  77,  76,  75,  74,  90,  88,  72,  71,  70,  69,  85,  87, 105,  83,  81,  82,  20,  19,  18,   2,
#--|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
    109,  61,  60,  59,  58, 106, 104,  56,  55,  54,  53, 101, 103,  25,  84,  65,  66,  52,  51,  50,  49,
#--|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
    108,  45,  44,  43,  42, 122, 120,  40,  39,  38,  37, 117,  21, 100,  99,  98,  97,
#--|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
    110, 124,  29,  28,  27,  26,  10,   8,  24,  23,  22,   5,  30, 113,  36,  35,  34,  33,
#--|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
     95, 112,   9,   0,  31,   1,   4,   3, 115, 114,
#--|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
]

keymap_ibm_iso = [[
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    KC.ESC,    KC.F1,  KC.F2,  KC.F3,  KC.F4,   KC.F5,  KC.F6,  KC.F7,  KC.F8,   KC.F9, KC.F10, KC.F11, KC.F12,   KC.PSCR, KC.SLCK,  KC.PAUS,
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    KC.GRV,  KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0,  KC.MINS,  KC.EQL,  KC.BSPC,    KC.INS, KC.HOME,  KC.PGUP,    KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS,
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    KC.TAB,    KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,  KC.Y,  KC.U,  KC.I,  KC.O,  KC.P, KC.LBRC, KC.RBRC,   KC.ENT,    KC.DEL,  KC.END,  KC.PGDN,    KC.P7,   KC.P8,   KC.P9,   KC.PENT,
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    KC.CLCK,    KC.A,  KC.S,  KC.D,  KC.F,  KC.G,  KC.H,  KC.J,  KC.K,  KC.L, KC.SCLN, KC.QUOT, KC.BSLS,                                         KC.P4,   KC.P5,   KC.P6,   KC.PSLS,
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    KC.LSFT, KC.NUBS,  KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,  KC.N,  KC.M,  KC.COMM,  KC.DOT,  KC.SLSH,    KC.RSFT,              KC.UP,              KC.P1,   KC.P2,   KC.P3,   KC.PENT,
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    KC.LCTL,        KC.LALT,                        KC.SPC,                       KC.RALT,            KC.RCTRL,   KC.LEFT, KC.DOWN, KC.RIGHT,    KC.P0,            KC.PDOT,
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
]]

keyboard.keymap = keymap_ibm_iso
keyboard.coord_mapping = coord_mapping

keyboard.debug_enabled = True

print("All loaded")

if __name__ == '__main__':
    keyboard.go()
