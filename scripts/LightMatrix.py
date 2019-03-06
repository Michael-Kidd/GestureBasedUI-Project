from sense_hat import SenseHat 
import threading
import time

def left(r, g, b):
    sense.set_pixel(3, 7, (r, g, b))
    sense.set_pixel(4, 7, (r, g, b))
    sense.set_pixel(3, 6, (r, g, b))
    sense.set_pixel(4, 6, (r, g, b))
    sense.set_pixel(2, 6, (r, g, b))
    sense.set_pixel(5, 6, (r, g, b))

def right(r, g, b):
    sense.set_pixel(3, 0, (r, g, b))
    sense.set_pixel(4, 0, (r, g, b))
    sense.set_pixel(3, 1, (r, g, b))
    sense.set_pixel(4, 1, (r, g, b))
    sense.set_pixel(2, 1, (r, g, b))
    sense.set_pixel(5, 1, (r, g, b))

def forward(r, g, b):
    sense.set_pixel(0, 3, (r, g, b))
    sense.set_pixel(0, 4, (r, g, b))
    sense.set_pixel(1, 3, (r, g, b))
    sense.set_pixel(1, 4, (r, g, b))
    sense.set_pixel(1, 2, (r, g, b))
    sense.set_pixel(1, 5, (r, g, b))

def reverse(r, g, b):
    sense.set_pixel(7, 3, (r, g, b))
    sense.set_pixel(7, 4, (r, g, b))
    sense.set_pixel(6, 3, (r, g, b))
    sense.set_pixel(6, 4, (r, g, b))
    sense.set_pixel(6, 2, (r, g, b))
    sense.set_pixel(6, 5, (r, g, b))

def clear():
    # Display these colours on the LED matrix
    sense.clear()

sense = SenseHat()