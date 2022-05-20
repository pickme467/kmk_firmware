print ("IBM Model M is starting")

import board

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
from kmk.kmk_keyboard import KMKKeyboard
from kmk.handlers.sequences import simple_key_sequence as sks

from kmk.extensions.solenoid import Solenoid

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

keyboard.col_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17,
                     board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26,)
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

coord_mapping = [
    119, 86, 85, 101, 117, 115, 113, 96, 80, 83, 67, 75, 76, 79, 63, 30,
    87, 71, 70, 69, 68, 84, 82, 66, 65, 64, 74, 90, 81, 99, 92, 94, 93, 27, 28, 29, 13,
    103, 55, 54, 53, 52, 100, 98, 50, 49, 48, 58, 106, 97, 19, 91, 78, 77, 59, 60, 61, 62,
    102, 39, 38, 37, 36, 116, 114, 34, 33, 32, 42, 122, 26, 107, 108, 109, 110,
    104, 118, 23, 22, 21, 20, 4, 2, 18, 17, 16, 10, 24, 126, 43, 44, 45, 46,
    89, 127, 3, 15, 25, 14, 11, 12, 124, 125,]

keymap_ibm_iso = [[
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    KC.ESC,    KC.F1,  KC.F2,  KC.F3,  KC.F4,    KC.F5,  KC.F6,  KC.F7,  KC.F8,    KC.F9, KC.F10, KC.F11, KC.F12,   KC.PSCR, KC.SLCK, KC.PAUS,
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    KC.GRV,  KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0,  KC.MINS,  KC.EQL,  KC.BSPC,     KC.INS,  KC.HOME, KC.PGUP,     KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS,
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    KC.TAB,    KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,  KC.Y,  KC.U,  KC.I,  KC.O,  KC.P, KC.LBRC, KC.RBRC, KC.ENT,       KC.DEL,  KC.END,  KC.PGDN,     KC.P7,   KC.P8,   KC.P9,   KC.PENT,
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    KC.CLCK,    KC.A,  KC.S,  KC.D,  KC.F,  KC.G,  KC.H,  KC.J,  KC.K,  KC.L, KC.SCLN, KC.QUOT, KC.BSLS,                                           KC.P4,   KC.P5,   KC.P6,   KC.PSLS,
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    KC.LSFT, KC.NUBS,  KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,  KC.N,  KC.M,  KC.COMM,  KC.DOT,  KC.SLSH,  KC.RSFT,                KC.UP,                KC.P1,   KC.P2,   KC.P3,   KC.PENT,
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    KC.LCTL,        KC.LALT,                        KC.SPC,                          KC.RALT, KC.RCTRL,             KC.LEFT, KC.DOWN, KC.RIGHT,    KC.P0,            KC.PDOT,
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ]]

keyboard.keymap = keymap_ibm_iso
keyboard.coord_mapping = coord_mapping

keyboard.debug_enabled = True

solenoid_ext = Solenoid()
keyboard.extensions.append(solenoid_ext)

print("All loaded")

if __name__ == '__main__':
    keyboard.go()
