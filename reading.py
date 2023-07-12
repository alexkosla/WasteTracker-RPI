"""Example of getting a direct reading from RPi.GPIO."""
# based on https://github.com/alaudet/hcsr04sensor/blob/master/recipes/basic_reading.py

import RPi.GPIO as GPIO
from hcsr04sensor import sensor
import datetime

# This script uses a static method inside the Measurement class
# called basic_distance
# No median readings pulled from a sample for error correction
# No setmode in the library
# No pin cleanups.  You handle all of these things in your own code
# Just a simple return of a cm distance as reported directly from Rpi.GPIO
# Only returns a metric value.

# set gpio pins
trig = 23
echo = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # use GPIO.BOARD for board pin values
x = sensor.Measurement
# use default temp of 20 Celcius
distance_default = x.basic_distance(trig, echo)

# example of passing temperature reading
# temperature affects speed of sound
# Easily combine with a temperature sensor to pass the current temp
temp = 25
distance_room_temp = x.basic_distance(trig, echo, celsius=temp)

print("The distance at  20 Celsius is {} cm".format(distance_default))
print("The distance at  25 Celsius is {} cm".format(distance_room_temp))

timestamp_curr = datetime.datetime.now()
print("the current time is {}".format(timestamp_curr))

# cleanup gpio pins.
GPIO.cleanup((trig, echo))