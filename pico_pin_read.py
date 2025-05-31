#This will need to be renamed to 'main.py' to run on power up of the Pi Pico.

from machine import Pin, ADC
from time import sleep
PinV = ADC(26)
out_pin = Pin(0, Pin.OUT)

while True:
    vInput = PinV.read_u16() / (3.3 * 65535)
    print(vInput)
    if vInput > 2:
        out_pin.high()
    else:
        out_pin.low()
    sleep(0.5)
