from machine import I2C,Pin
import utime

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
devices = i2c.scan()

if devices:
    print('I2C devices found:',devices)
else:
    print('no I2C devices found')
