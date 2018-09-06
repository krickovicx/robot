import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

gpio.output(7, True)
time.sleep(0.5)
gpio.output(7, False)
gpio.output(11, True)
time.sleep(0.5)
gpio.output(11, False)
gpio.output(15, True)
time.sleep(0.5)
gpio.output(15, False)
gpio.output(13, True)
time.sleep(0.5)
gpio.output(13, False)
gpio.cleanup()
