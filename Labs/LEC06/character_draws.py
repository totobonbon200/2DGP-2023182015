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

# 캔버스 생성
open_canvas(800, 600)


# 바뀌는 캐릭터 위치
a = 0
while True:
    
    move_circle()
    move_rectangle()
    move_triangle()
    delay(0.5)
    a = a + 1
    pass