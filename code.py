import time
import usb_hid
import digitalio
import board
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

keyboard = Keyboard(usb_hid.devices)

def do_string(string):
    for x in string:
        if x == '/':
            key = Keycode.FORWARD_SLASH
        elif x == '\\':
            key = Keycode.BACKSLASH
        elif  x == ':':
            keyboard.press(Keycode.LEFT_SHIFT,Keycode.SEMICOLON)  
            time.sleep(0.1)
            keyboard.release_all()
            return
        elif  x == '.':
            key = Keycode.PERIOD
        else:    
            key = getattr(Keycode, x.upper())
        keyboard.press(key)
        keyboard.release(key)
        time.sleep(0.1)
    

def press_and_release(command):
    key = getattr(Keycode, command.upper())
    keyboard.press(key)
    keyboard.release(key)
    time.sleep(0.4)

        

    
press_and_release("windows")
do_string("edge")
press_and_release("enter")
keyboard.press(Keycode.ALT,Keycode.D)
keyboard.release_all()
do_string("www.youtube.com/watch?v=dQw4w9WgXcQ")
press_and_release("enter")


