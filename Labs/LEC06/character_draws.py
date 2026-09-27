from pico2d import *
import math

# 캔버스 크기
canvas_x = 800
canvas_y = 600
# 캐릭터 위치
character_x = canvas_x / 2
character_y = canvas_y / 2
# 딜레이
dy = 0.01
# 삼각형 점
point1 = [100, 100]
point2 = [700, 100]
point3 = [400, 500]

# 캔버스 생성
open_canvas(canvas_x, canvas_y)

# 이미지 로드
grass = load_image('grass.png')
character = load_image('character.png')

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(dy)

def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = character_x + 200 * math.cos(theta)
        y = character_y + 200 * math.sin(theta)
        draw_character(x, y)

def move_top():
    for x in range(50, 751, 5):
        draw_character(x, 550)

def move_right1():
    for y in range(300, 49, -5):
        draw_character(750, y)

def move_right2():
    for y in range(550, 300, -5):
        draw_character(750, y)

def move_bottom():
    for x in range(750, 49, -5):
        draw_character(x, 50)

def move_left():
    for y in range(50, 551, 5):
        draw_character(50, y)

def move_rectangle():
    move_right1()
    move_bottom()
    move_left()
    move_top()
    move_right2()

def move_between(start_x, start_y, end_x, end_y):
    steps = 120
    for step in range(steps + 1):
        t = step / steps
        x = start_x + (end_x - start_x) * t
        y = start_y + (end_y - start_y) * t
        draw_character(x, y)



def move_triangle():
    move_between(point1[0], point1[1], point2[0], point2[1])
    move_between(point2[0], point2[1], point3[0], point3[1])
    move_between(point3[0], point3[1], point1[0], point1[1])

while True:
    #move_circle()
    #move_rectangle()
    move_triangle()

close_canvas()