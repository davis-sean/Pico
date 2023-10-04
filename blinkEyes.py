from machine import Pin
from time import sleep

eyes_quantity = 3

class Eye:

	def __init__(self, eye_number, light_on):
		self.number = eye_number
		self.on = light_on
		self.led = Pin(eye_number, Pin.OUT)

	def open(self):
		self.on = True

	def close(self):
		self.on = False

eyes = []

for i in range(eyes_quantity):
    eyes.append(Eye(i, True))

for i in eyes:
    print(i.number)
    print(i.on)
    # Eye.led(i)
