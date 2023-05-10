# code.py for MouseWiggler
import usb_hid
from adafruit_hid.mouse import Mouse
from time import sleep
import board
import digitalio

mouse=Mouse(usb_hid.devices)
boardLed=digitalio.DigitalInOut(board.LED)
boardLed.direction=digitalio.Direction.OUTPUT

while True:
    mouse.move(-1, 0, 0)
    mouse.move(1, 0, 0)
    for i in range(30):
        boardLed.value=True;
        sleep(0.5)
        boardLed.value=False;
        sleep(0.5)
