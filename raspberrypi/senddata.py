# this is the program on board the pi that then sends the data to the backend after getting it from the esp32
import requests
import gpioRead


def main_json_output(temperature_pin, ppm_pin, lightLevels_pin, boilerOn_pin):
  
  # establishing the headers for the http request and getting data from the backend
  uid_headers = {'method': 'GET'}
  uid = requests.get('https://jeremypetch.com/uuid', headers=json.dumps(uid_headers))

  
  # dumps a data dictionary as a json object
  # will be data from the esp32 sensor readings
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

headers = {'Content-Type': 'application/json'}
r = requests.post('https://jeremypetch.com/append', headers=headers, json=gpioRead.main_json_output())