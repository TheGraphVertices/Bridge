import requests
# from gpioRead import data

headers = {'content-type': 'json'}
r = requests.post('https://jeremypetch.com/append', headers=headers, json=data)