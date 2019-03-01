from sense_hat import SenseHat 

def left():
    sense.set_pixel(3, 7, (0, 255, 0))
    sense.set_pixel(4, 7, (0, 255, 0))
    sense.set_pixel(3, 6, (0, 255, 0))
    sense.set_pixel(4, 6, (0, 255, 0))
    sense.set_pixel(2, 6, (0, 255, 0))
    sense.set_pixel(5, 6, (0, 255, 0))

def right():
    sense.set_pixel(3, 0, (0, 255, 0))
    sense.set_pixel(4, 0, (0, 255, 0))
    sense.set_pixel(3, 1, (0, 255, 0))
    sense.set_pixel(4, 1, (0, 255, 0))
    sense.set_pixel(2, 1, (0, 255, 0))
    sense.set_pixel(5, 1, (0, 255, 0))

def forward():
    sense.set_pixel(0, 3, (0, 0, 255))
    sense.set_pixel(0, 4, (0, 0, 255))
    sense.set_pixel(1, 3, (0, 0, 255))
    sense.set_pixel(1, 4, (0, 0, 255))
    sense.set_pixel(1, 2, (0, 0, 255))
    sense.set_pixel(1, 5, (0, 0, 255))

def reverse():
    sense.set_pixel(7, 3, (255, 0, 0))
    sense.set_pixel(7, 4, (255, 0, 0))
    sense.set_pixel(6, 3, (255, 0, 0))
    sense.set_pixel(6, 4, (255, 0, 0))
    sense.set_pixel(6, 2, (255, 0, 0))
    sense.set_pixel(6, 5, (255, 0, 0))

def clear():
    # Display these colours on the LED matrix
    sense.clear()



sense = SenseHat()
clear()
left()
right()
forward()
reverse()