import storage
import usb_hid

# Disable mass storage device
storage.disable_usb_drive()

# Enable HID (keyboard/mouse/etc.)
usb_hid.enable((usb_hid.Device.KEYBOARD,))
