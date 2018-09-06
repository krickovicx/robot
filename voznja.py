import RPi.GPIO as gpio
import time
import curses
import os

screen = curses.initscr(); curses.noecho(); curses.cbreak(); screen.keypad(True)

gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT); gpio.setup(11, gpio.OUT); gpio.setup(13, gpio.OUT); gpio.setup(15, gpio.OUT)
gpio.setup(12, gpio.OUT);
def stop():
	gpio.output(7, False)
        gpio.output(13, False)
        gpio.output(11, False)
        gpio.output(15, False)

try:
    gpio.output(12, True) 
    while True:
        char = screen.getch()
        if char == ord('i'):
            break
        if char == ord('S'):
            os.system('sudo shutdown now')
        elif char == curses.KEY_UP:
	    stop()
            gpio.output(7, True)
	    gpio.output(13, True)
	elif char == curses.KEY_DOWN:
	    stop()
	    gpio.output(11, True)
	    gpio.output(15, True)
	elif char == curses.KEY_LEFT:
	    stop()
	    gpio.output(11, True)
	    gpio.output(13, True)
	elif char == curses.KEY_RIGHT:
	    stop()
	    gpio.output(7, True)
	    gpio.output(15, True)
        elif char == 32:
	    stop()

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo(); curses.endwin(); 
    gpio.output(7, False); gpio.output(11, False); gpio.output(13, False); gpio.output(15, False); gpio.cleanup()


