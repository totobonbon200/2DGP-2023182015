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

def move_circle():
    print(f"circle ({math.cos(a)}, {math.sin(a)})")
    pass

def move_rectangle():
    print(f"rectangle")
    pass

def move_triangle():
    print(f"triangle")
    pass

clear_canvas()
character.draw(character_x, character_y)
update_canvas()

# 바뀌는 캐릭터 위치
a = 0
while True:
    clear_canvas()
    character.draw(character_x, character_y)
    update_canvas()

    move_circle()
    move_rectangle()
    move_triangle()
    delay(0.5)
    a = a + 1
    pass

close_canvas()