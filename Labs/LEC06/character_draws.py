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

def move_rectangle():
    pass

def move_triangle():
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()