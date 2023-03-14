#  this program is for the esp32 to read the gpio inputs and return the data as a json object
# can be made to return dictionary if json.dumps needs to be done on the pi

# esp32 has adc converters on pins 32-39
# https://www.youtube.com/watch?v=joA9RvlO294

# importing the necessary libraries for the GPIO/server/component communication, as well as the time for the json data
import json
from machine import Pin, 
import datetime
import requests


# assigning gpio pin roles to read sensor inputs
# still need pins assigning
temperature_pin = Pin(None, Pin.IN)
ppm_pin = Pin(None, Pin.IN)
lightLevels_pin = Pin(None, Pin.IN)
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

