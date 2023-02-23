#  this program is for the esp32 to read the gpio inputs and return the data as a json object
# can be made to return dictionary if json.dumps needs to be done on the pi

# importing the necessary libraries for the GPIO/server/component communication, as well as the time for the json data
import json
# from machine import pin
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

def main_json_output(temperature_pin, ppm_pin, lightLevels_pin, boilerOn_pin):
  
  # establishing the headers for the http request and getting data from the backend
  uid_headers = {'method': 'GET'}
  uid = requests.get('https://jeremypetch.com/uuid', headers=json.dumps(uid_headers))

  
  # dumps a data dictionary as a json object
  data = {
    "temp": tempread(temperature_pin),
    "ppm": ppmread(ppm_pin),
    "light": lightread(lightLevels_pin),
    "boiler": boilerread(boilerOn_pin),
    "UID": uid,
    "time": str(datetime.datetime.now(datetime.timezone.utc).isoformat())
  }

  # can be removed to just return the dictionary
  data = json.dumps(data)

  
  # establishing the headers for the http request and getting data from the backend
  # this is not correct the data needs to be sent to the pi prior to http post
  headers = {'Content-Type': 'application/json', 'method': 'POST'}
  requests.post('https://jeremypetch.com/append', headers=json.dumps(headers), json=data)

  return data

if "__name__" == "__main__":
  print(main_json_output())