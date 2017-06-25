import RPi.GPIO as gpio
import dht11
import datetime

# initialize GPIO
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.cleanup()

# read data using pin 5
instance = dht11.DHT11(pin = 5)


try:
    while True:
        result = instance.read()
        if result.is_valid():
            temp = result.temperature
            hum = result.humidity
            
            print(temp)
            f = open("temperature.txt", "w")
            f.write(str(temp))
            f.close()

            print(hum)
            f = open("humidity.txt", "w")
            f.write(str(hum))
            f.close()
            
except KeyboardInterrupt:
    gpio.cleanup()
