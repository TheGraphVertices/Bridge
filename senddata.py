# this is the program on board the pi that then sends the data to the backend after getting it from the esp32
import requests
import gpioRead


headers = {'Content-Type': 'application/json'}
r = requests.post('https://jeremypetch.com/append', headers=headers, json=data)