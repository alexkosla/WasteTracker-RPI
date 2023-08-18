"""Example of getting a direct reading from RPi.GPIO."""
# edit: based on https://github.com/alaudet/hcsr04sensor/blob/master/recipes/basic_reading.py
# comments beginning with edit: describe portions of code modified/created by Alex Kosla

import RPi.GPIO as GPIO
from hcsr04sensor import sensor
import datetime
import requests 
import json

# This script uses a static method inside the Measurement class
# called basic_distance
# No median readings pulled from a sample for error correction
# No setmode in the library
# No pin cleanups.  You handle all of these things in your own code
# Just a simple return of a cm distance as reported directly from Rpi.GPIO
# Only returns a metric value.

# set gpio pins
# edit: changed pins to match the ones I'm using 
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
# edit: using 25C as this is my approximate room temperature, rather than 20C
temp = 25
distance_room_temp = x.basic_distance(trig, echo, celsius=temp)

print("The distance at  20 Celsius is {} cm".format(distance_default))
print("The distance at  25 Celsius is {} cm".format(distance_room_temp))

# cleanup gpio pins.
GPIO.cleanup((trig, echo))

# edit: All of the following code is mine.

# edit: Format the current time into a java-parseable format
timestamp_curr = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
print("the current time is {}".format(timestamp_curr))

# edit: store data as a dict, so it can be easily serialized into json
data = {}
data['distance'] = distance_default
data['time'] = timestamp_curr
body = json.dumps(data, default=str)
print(body)

# edit: hardcoded IP to access web server via POST
post_url = "http://192.168.0.199:8080/readings/create"
response = requests.post(post_url, data=body, headers={"Content-Type": "application/json"})

# print an error if the POST is unsuccessful
if response.status_code != 200:
    print("Error: {}".format(response.status_code))

print(response.text)