from machine import pin
import time 

x = Pin(25, Pin.OUT)
#names x as pin for quick reference

while True:
  x.value(1)
  x.value(0)
  x.value(1)
  x.value(0)
#Turns led on and off in a blinking motion, alerts user code has been recieved/transmitted
