from pico2d import *
import math

# 캔버스 생성
open_canvas(800, 600)

# 이미지 로드
character = load_image('character.png')

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.05)

def move_circle():
    for degree in range(0, 360, 20):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_character(x, y)
    pass

def move_top():
    print(f"top")
    for x in range(50, 750, 20):
        draw_character(x, 550)
    pass

def move_right():
    print(f"right")
    for y in range(550, 50, -20):
        draw_character(750, y)
    pass

def move_bottom():
    print(f"bottom")
    for x in range(750, 50, -20):
        draw_character(x, 50)
    pass

def move_left():
    print(f"left")
    for y in range(50, 550, 20):
        draw_character(50, y)
    pass

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_between(start_x, start_y, end_x, end_y):
    for step in range(120 + 1):
        t = step / 120
        x = start_x + (end_x - start_x) * t
        y = start_y + (end_y - start_y) * t
        draw_character(x, y)

def move_triangle():
    move_between(400, 550, 750, 50)
    move_between(750, 50, 50, 50)
    move_between(50, 50, 400, 550)
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    print(f"cycling")
    pass

close_canvas()