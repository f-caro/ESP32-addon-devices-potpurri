# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C
import ssd1306
from time import sleep

# ESP32 Pin assignment 
##### check new docs!!! i2c = machine.SoftI2C(-1, scl=Pin(10), sda=Pin(15))
i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
#i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 32  # Screen size is 32 pixels high, but framebuf.text() auto scales it somewhere
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
oled.show()

i = 0
while (1):
    #oled.fill(0)
    #oled.show()
    i = i + 1
    i = i%32
    oled.text('PROMEL LTDA', 0, i, 0)
    oled.show()
    oled.text('PROMEL LTDA', 0, i+1, 1)
    oled.show()
    #sleep(1)


