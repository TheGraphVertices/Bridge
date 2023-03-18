#  this program is for the esp32 to read the gpio inputs and return the data as a json object
# can be made to return dictionary if json.dumps needs to be done on the pi

# esp32 has adc converters on pins 32-39
# https://www.youtube.com/watch?v=joA9RvlO294
# https://www.youtube.com/watch?v=4XPDyKujcxI

# importing the necessary libraries for the GPIO/server/component communication, as well as the time for the json data
# imports on the microcontrollers by default
from machine import Pin
from time import sleep
# imports included through the installation of additional libraries on the CircuitPython esp32s
import json
import requests
import adafruit_dht
from MQ2 import MQ2

# assigning gpio pin roles to read sensor inputs
class Gas_sensor:
  # class in order to use the MQ2 gas sensor hardware
	def __init__(self, pin=7):
		self.sensor = MQ2(pinData=pin, baseVoltage=3.3)
    self.sensor.calibrate()
    self.base_resistance = self.sensor._ro

	def get_current_smoke(self):
    current_smoke = self.sensor.readSmoke()
    change_percentage = (current_smoke - self.base_resistance) / 100
    return change_percentage



gas_sensor = Gas_sensor()
dht_device = adafruit_dht.DHT22(8)

def tempread(dht_device):
  # use the dht module to return a value for temp from the dht11 sensor
  temperature = dht_device.temperature
  return temperature
  
def current_smoke_read(gas_sensor):
  # use the MQ2 gas sensor input to return a value for various gases
  # the gas sensor used has a 2 minute heat up window so initial readings of ppm will be inaccurate
  return int(gas_sensor.get_current_smoke())
  
def humidity(dht_device):
  # use the dht module to return a value for temp from the dht11 sensor
  humidity = dht_device.humidity
  return humidity

def main_json_output(dht_device, gas_sensor):
  
  # establishing the headers for the http request and getting data from the backend, for the sake of demonstration the uid has already been determined
  # uid_headers = {'method': 'GET'}
  # uid = requests.get('https://jeremypetch.com/user', headers=json.dumps(uid_headers))

  # test_uid for demo
  uid = 'f87ca9c0-5263-498c-a3ee-f330c6515868'
  # dumps a data dictionary as a json object
  # data from the esp32 sensor readings
  data = {
  "uid": uid,   
  "temp": tempread(dht_device),
  "ppm": current_smoke_read(gas_sensor),
  "humidity": humidity(dht_device),
}

  # turning the python dict into json 
  data = json.dumps(data)

  
  # establishing the headers for the http request and getting response from the backend
  headers = {'Content-Type': 'application/json', 'method': 'POST'}
  requests.post('https://jeremypetch.com/data', headers=json.dumps(headers), json=data)


if __name__ == '__main__':
  while True:
    main_json_output(dht_device, gas_sensor)
    sleep(300)
    