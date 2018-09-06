import RPi.GPIO as gpio
import time
import curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)

try:
    while True:
        char = screen.getch()
        if char == ord('i'):
            break
        elif char == curses.KEY_UP:
            gpio.output(7, True)
        elif char == curses.KEY_DOWN:
            gpio.output(7, False)

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo(); curses.endwin(); 
    gpio.output(7, False); gpio.cleanup()


