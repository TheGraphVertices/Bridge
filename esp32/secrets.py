# User's local wifi network for the esp32s to use, stored in a seperate file to the main code so that they can be changed despite the time.sleep() in the main.py

secrets = {
  'ssid': 'home_wifi_network',
  'password': 'wifi_password',
}
