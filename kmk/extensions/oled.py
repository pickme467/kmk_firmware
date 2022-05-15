from kmk.extensions import Extension
from kmk.kmktime import PeriodicTimer

# OLED
import busio
import board
import adafruit_ssd1306

class OLED(Extension):

    def __init__(self, custom_lines, custom_oled_off=5):
        self.lines = custom_lines
        self.oled_off_sec = custom_oled_off
        self._i2c = busio.I2C(board.GP27, board.GP26)
        self._oled = adafruit_ssd1306.SSD1306_I2C(128, 32, self._i2c)
        self.display_text()

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):
        self._set_timer()

    def before_matrix_scan(self, sandbox):
        return

    def after_matrix_scan(self, sandbox):
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        if sandbox.matrix_update != None:
            self.display_text()
        elif self._timer.tick() == True:
            self.hide_text()

    def on_powersave_enable(self, sandbox):
        self.hide_text()
        return

    def on_powersave_disable(self, sandbox):
        self.display_text()

    def display_text(self):
        row = 0
        col = 0

        for t in self.lines:
            if col > 2:
                break
            self._oled.text(t, 0, row, 1)
            row += 12
            col += 1

        self._oled.show()
        self._set_timer()

    def hide_text(self):
        self._oled.fill(0)
        self._oled.show()

    def _set_timer(self):
        self._timer = PeriodicTimer(1000 * self.oled_off_sec)
