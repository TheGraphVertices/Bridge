#  this program is for the esp32 to read the gpio inputs and return the data as a json object
# can be made to return dictionary if json.dumps needs to be done on the pi

# esp32 has adc converters on pins 32-39
# https://www.youtube.com/watch?v=joA9RvlO294
# https://www.youtube.com/watch?v=4XPDyKujcxI

# importing the necessary libraries for the GPIO/server/component communication, as well as the time for the json data
import json
from machine import Pin, ADC
import datetime
import requests


# assigning gpio pin roles to read sensor inputs
# still need pins assigning
temperature_pin = ADC(Pin(32))
ppm_pin = ADC(Pin(33))
lightLevels_pin = ADC(Pin(34))
boilerOn_pin = Pin(None, Pin.IN)

def tempread(temperature_pin):
  # use the temperature_pin input to return a value
  pass
  
def ppmread(ppm_pin):
  # use the temperature_pin input to return a value
  pass
  
def lightread(lightLevels_pin):
  pass

def boilerread(boilerOn_pin):
  pass



response = requests.post('https://pythonexamples.org/', data = {'key':'value'})