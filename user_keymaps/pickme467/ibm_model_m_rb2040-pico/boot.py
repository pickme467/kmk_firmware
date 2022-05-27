import supervisor
supervisor.set_next_stack_limit(4096 + 4096)

import board
import digitalio
import storage
import usb_cdc
import usb_hid

# If this key is held during boot, don't run the code which hides the storage and disables serial
col = digitalio.DigitalInOut(board.GP2)
row = digitalio.DigitalInOut(board.GP8)

col.switch_to_output(value=True)
row.switch_to_input(pull=digitalio.Pull.DOWN)

if not row.value:
    storage.disable_usb_drive()
    # Equivalent to usb_cdc.enable(console=False, data=False)
    # usb_cdc.disable()
    # usb_hid.enable(boot_device=1)
    pass

row.deinit()
col.deinit()
