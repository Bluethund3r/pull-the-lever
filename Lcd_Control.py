from machine import Pin, I2C
from time import sleep
from i2c_lcd import I2cLcd

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = 39
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

lcd.hal_write_command(0x0F)
#Creates Blinking Cursor On Screen
 
lcd.putstr('Greetings From Another Realm')
