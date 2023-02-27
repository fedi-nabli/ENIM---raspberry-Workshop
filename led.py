import RPi.GPIO as GPIO
import time
import board
import adafruit_dht

GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)
sensor = adafruit_dht.DHT11(board.D23)

while True:
  temp = sensor.temperature
  humidity = sensor.humidity
  print(f"Temperature: {temp}°C   Humidity: {humidity}% ")

  print("Led on")
  GPIO.output(8, GPIO.HIGH)
  time.sleep(2)

  print("Led Off")
  GPIO.output(8, GPIO.LOW)
  time.sleep(1)
