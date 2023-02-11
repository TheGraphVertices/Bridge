import json
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

for i in range(50):
  GPIO.output(18, GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(18, GPIO.LOW)
  time.sleep(0.5)