import time
from random import randrange
import RPi.GPIO as gpio
from firebase import firebase

# Import library
import MAX7219array as m7219
# Import fonts
from MAX7219fonts import CP437_FONT, SINCLAIRS_FONT, LCD_FONT, TINY_FONT

# The following imported variables make it easier to feed parameters to the library functions
from MAX7219array import DIR_L, DIR_R, DIR_U, DIR_D
from MAX7219array import DIR_LU, DIR_RU, DIR_LD, DIR_RD
from MAX7219array import DISSOLVE, GFX_ON, GFX_OFF, GFX_INVERT

# initialize GPIO
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.cleanup()

# Initialise the library and the MAX7219/8x8LED array
m7219.init()

green_pin = 26 # normal
red_pin = 19 # hot
blue_pin = 5 # cold
yellow_pin = 13 # gas
white_pin = 12 # environment

gpio.setmode(gpio.BCM)
gpio.setup(green_pin, gpio.OUT)
gpio.setup(red_pin, gpio.OUT)
gpio.setup(blue_pin, gpio.OUT)
gpio.setup(yellow_pin, gpio.OUT)
gpio.setup(white_pin, gpio.OUT)

gpio.output(green_pin, True)
gpio.output(red_pin, True)
gpio.output(blue_pin, True)
gpio.output(yellow_pin, True)
gpio.output(white_pin, True)

m7219.scroll_message_horiz("Hello", 1, 5, DIR_L, CP437_FONT)

firebase = firebase.FirebaseApplication('https://ohmybaby-60436.firebaseio.com', None)

try:
    while True:
        Temp = firebase.get('/temp', 'temp')
        Humi = firebase.get('/humi', 'humi')
        Max = firebase.get('/max', 'max')
        Min = firebase.get('/min', 'min')
        Gas = firebase.get('/gas', 'gas')

        #discomfort = (float)(9.0/5.0)*Temp - 0.55*(1.0 - Humi)*((9.0/5.0)*Temp - 26.0) + 32.0
        if(Temp >= 28 or Temp <= 18 or Humi <= 10 or Humi >= 60): 
            gpio.output(white_pin, True)
            gpio.output(green_pin, False)
            #m7219.scroll_message_horiz("Discomfort ", 1, 5, DIR_L, CP437_FONT)
            #m7219.clear_all()
        else:
            gpio.output(white_pin, False)
            
        if(Max >= 8300):
            gpio.output(red_pin, True)
            gpio.output(green_pin, False)
        else:
            gpio.output(red_pin, False)
            
        if(Min <= 7800):
            gpio.output(blue_pin, True)
            gpio.output(green_pin, False)
        else:
            gpio.output(blue_pin, False)
            
        if(Gas == 1):
            gpio.output(yellow_pin, True)
            gpio.output(green_pin, False)
        else:
            gpio.output(yellow_pin, False)

        if(Temp < 28 and Temp > 18 and Humi > 10 and Humi < 60 and Max < 8300 and Min > 7800 and Gas == 0):
            gpio.output(green_pin, True)
            gpio.output(red_pin, False)
            gpio.output(yellow_pin, False)
            gpio.output(blue_pin, False)
            gpio.output(white_pin, False)

        print(Temp)
        print(Humi)
        print(Max)
        print(Min)
        print(Gas)
            
except KeyboardInterrupt:
    gpio.cleanup()
    m7219.scroll_message_horiz("Goodbye!", 1, 8)
    m7219.clear_all()
    gpio.output(green_pin, False)
    gpio.output(red_pin, False)
    gpio.output(yellow_pin, False)
    gpio.output(blue_pin, False)
    gpio.output(white_pin, False)
