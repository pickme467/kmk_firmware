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
        self.i2c = busio.I2C(board.GP27, board.GP26)
        self.oled = adafruit_ssd1306.SSD1306_I2C(128, 32, self.i2c)
        self.display_text()


    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):
        self.set_timer()

    def before_matrix_scan(self, sandbox):
        return

    def after_matrix_scan(self, sandbox):
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        if self._timer.tick() == True:
            self.hide_text()

    def on_powersave_enable(self, sandbox):
        self.hide_text()
        return

    def on_powersave_disable(self, sandbox):
        self.display_text()

    def set_timer(self):
        self._timer = PeriodicTimer(1000 * self.oled_off_sec)

    def display_text(self):
        row = 0
        col = 0

        for t in self.lines:
            if col > 2:
                break
            self.oled.text(t, 0, row, 1)
            row += 12
            col += 1

        self.oled.show()
        self.set_timer()

    def hide_text(self):
        self.oled.fill(0)
        self.oled.show()
