#  this program is for the esp32 to read the gpio inputs and return the data as a json object to a backend endpoint

# importing the necessary libraries for the GPIO/server/component communication, as well as the time for the json data
# imports on the microcontrollers by default
from machine import Pin
from time import sleep
# imports included through the installation of additional libraries on the CircuitPython esp32s for their respective purposes
import json
import requests
import adafruit_dht
from MQ2 import MQ2
import ipaddress
import ssl
import wifi
import socketpool
import adafruit_requests
# the data needed for internet connection must be provided by the user (internet name and password in the secrets.py file)
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

def web_client_connect_and_test(secrets):
  # uses user-input data (in secrets.py for the connection to their local wifi)
  # this is the necessary code for the esp32s to connect to the internet for the POST and GET requests in the program (sampled from adafruit docs), however for the sake of demonstration this step was abstracted for simplicity
  # URLs to fetch from
  TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"
  JSON_QUOTES_URL = "https://www.adafruit.com/api/quotes.php"
  JSON_STARS_URL = "https://api.github.com/repos/adafruit/circuitpython"
  
  # Get wifi details and more from a secrets.py file
  try:
      from secrets import secrets
  except ImportError:
      print("WiFi secrets are kept in secrets.py, please add them there!")
      raise
  
  print("ESP32-S2 WebClient Test")
  
  print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])
  
  print("Available WiFi networks:")
  for network in wifi.radio.start_scanning_networks():
      print("\t%s\t\tRSSI: %d\tChannel: %d" % (str(network.ssid, "utf-8"),
              network.rssi, network.channel))
  wifi.radio.stop_scanning_networks()
  
  print("Connecting to %s"%secrets["ssid"])
  wifi.radio.connect(secrets["ssid"], secrets["password"])
  print("Connected to %s!"%secrets["ssid"])
  print("My IP address is", wifi.radio.ipv4_address)
  
  ipv4 = ipaddress.ip_address("8.8.4.4")
  print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))
  
  pool = socketpool.SocketPool(wifi.radio)
  requests = adafruit_requests.Session(pool, ssl.create_default_context())
  
  print("Fetching text from", TEXT_URL)
  response = requests.get(TEXT_URL)
  print("-" * 40)
  print(response.text)
  print("-" * 40)
  
  print("Fetching json from", JSON_QUOTES_URL)
  response = requests.get(JSON_QUOTES_URL)
  print("-" * 40)
  print(response.json())
  print("-" * 40)
  
  print()
  
  print("Fetching and parsing json from", JSON_STARS_URL)
  response = requests.get(JSON_STARS_URL)
  print("-" * 40)
  print("CircuitPython GitHub Stars", response.json()["stargazers_count"])
  print("-" * 40)
  
  print("done")
  



# assigning gpio pin roles to read sensor inputs
class Gas_sensor:
  # class in order to use the MQ2 gas sensor hardware
	def __init__(self, pin=7):
		self.sensor = MQ2(pinData=pin, baseVoltage=3.3)


	def get_current_smoke(self):
    self.sensor.calibrate()
    self.base_resistance = self.sensor._ro
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
  # uid = requests.get('https://api.jeremypetch.com/user', headers=json.dumps(uid_headers))

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

  
  # establishing the headers for the http request and getting response from the backend using a wifi connection
  headers = {'Content-Type': 'application/json', 'method': 'POST'}
  requests.post('https://api.jeremypetch.com/data', headers=json.dumps(headers), json=data)


if __name__ == '__main__':
  while True:
    main_json_output(dht_device, gas_sensor) # outputs the reading of the sensors to the backend every 5 minutes (300 seconds) as long as the microcontrollers are connected to the internet
    sleep(300)
    