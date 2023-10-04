from machine import Pin
from time import sleep

light = Pin("LED", Pin.OUT)
button = Pin(4, Pin.IN, Pin.PULL_UP )
led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)
led4 = Pin(3, Pin.OUT)

State=0

light.value(1)

while True:
    if button.value() == 0:
        if State==0:
            led1.value(1)
            led2.value(1)
            led3.value(1)
            led4.value(1)
            sleep_ms=100
            while button.value() == 0:
                State=1
        else:
            led1.value(0)
            led2.value(0)
            led3.value(0)
            led4.value(0)
            sleep_ms=100
            while button.value() == 0:
                State=0

