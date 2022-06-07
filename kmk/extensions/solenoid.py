from kmk.extensions import Extension
from kmk.kmktime import PeriodicTimer

import board
import digitalio

class Solenoid(Extension):

    def __init__(self, solenoid_pin, led_pin):
        self.solenoid = digitalio.DigitalInOut(solenoid_pin)
        self.solenoid.direction = digitalio.Direction.OUTPUT
        self.solenoid.value = False
        self._timer = None
        self._timer_period = 5
        if None != led_pin:
            self.led = digitalio.DigitalInOut(led_pin)
            self.led.direction = digitalio.Direction.OUTPUT
            self.led.value = False
        else:
            self.led = None

    def on_runtime_enable(self, sandbox):
        self.solenoid.value = False
        return

    def on_runtime_disable(self, sandbox):
        self.solenoid.value = False
        return

    def during_bootup(self, sandbox):
        self.solenoid.value = False
        return

    def before_matrix_scan(self, sandbox):
        return

    def after_matrix_scan(self, sandbox):
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        if sandbox.matrix_update != None:
            if sandbox.matrix_update.pressed == True:
                self._solenoid_on()
        self._solenoid_off()

    def on_powersave_enable(self, sandbox):
        self.solenoid.value = False
        return

    def on_powersave_disable(self, sandbox):
        self.solenoid.value = False
        return

    def _solenoid_on(self):
        if self._timer == None:
            self.solenoid.value = True
            self._timer = PeriodicTimer(self._timer_period)
        if None != self.led:
            self.led.value = True

    def _solenoid_off(self):
        if self._timer == None or self._timer.tick() == True:
            self.solenoid.value = False
            self._timer = None
        if None != self.led:
            self.led.value = False
