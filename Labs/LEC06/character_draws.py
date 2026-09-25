from pico2d import *
import math

def move_circle():
    print(f"circle")
    pass

def move_rectangle():
    print(f"rectangle")
    pass

def move_triangle():
    print(f"triangle")
    pass

a = 0

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    print("position ({c} {s})".format(c=math.cos(a), s=math.sin(a)))
    delay(0.5)
    a = a + 1
    pass