# Add your Python code here. E.g.
from microbit import *
uart.init(baudrate=115200, bits=8, parity=None, stop=1, tx=pin1, rx=pin2)

while True:
    display.scroll(uart.readall())
    if button_a.is_pressed():
        uart.write('he')
