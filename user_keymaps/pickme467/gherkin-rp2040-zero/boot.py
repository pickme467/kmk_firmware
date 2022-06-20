import supervisor
supervisor.set_next_stack_limit(4096 + 4096)

import board
import digitalio
import storage
import usb_cdc
import usb_hid

# Top left key on gherkin keyboard
col = digitalio.DigitalInOut(board.GP12)
row = digitalio.DigitalInOut(board.GP1)

col.switch_to_output(value=True)
row.switch_to_input(pull=digitalio.Pull.DOWN)

if not row.value:
    storage.disable_usb_drive()
    # Equivalent to usb_cdc.enable(console=False, data=False)
    usb_cdc.disable()
    pass

# Enable keyboard at boot
print('Enabling keyboard at boot')
usb_hid.enable(boot_device=1)

row.deinit()
col.deinit()

print('Boot done')
