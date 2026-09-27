from pico2d import *
import math

# 캔버스 크기
canvas_x = 800
canvas_y = 600
character_x = canvas_x / 2
character_y = canvas_y / 2

# 캔버스 생성
open_canvas(canvas_x, canvas_y)

# 이미지 로드
grass = load_image('grass.png')
character = load_image('character.png')

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = character_x + 200 * math.cos(theta)
        y = character_y + 200 * math.sin(theta)
        draw_character(x, y)

def move_top():
    for x in range(50, 751, 5):
        draw_character(x, 550)

def move_right():
    for y in range(550, 49, -5):
        draw_character(750, y)

def move_bottom():
    for x in range(750, 49, -5):
        draw_character(x, 50)

def move_left():
    for y in range(50, 551, 5):
        draw_character(50, y)

def move_rectangle():
    move_right()
    move_bottom()
    move_left()
    move_top()

def move_between(start_x, start_y, end_x, end_y):
    steps = 120
    #for step in range(steps + 1):
    draw_character(x, y)

def move_triangle():
    
    pass

while True:
    move_circle()
    move_rectangle()
    #move_triangle()

close_canvas()