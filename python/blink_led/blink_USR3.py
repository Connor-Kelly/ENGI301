import Adafruit_BBIO.GPIO as GPIO
import time

# for i in range(4):
GPIO.setup("USR3", GPIO.OUT)

while True:
    # for i in range(4):
    GPIO.output("USR3", GPIO.HIGH)
    time.sleep(1/10)

    # for i in range(4):
    GPIO.output("USR3", GPIO.LOW)
    time.sleep(1/10)
