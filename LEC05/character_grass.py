from pico2d import *
import math

open_canvas(800, 600)


# 여기를 채우시오.
grass = load_image('grass.png')
character = load_image('character.png')

grass.draw(400, 30)
character.draw(400, 90)

r = 80
a = 0
while 1:
    for i in range(40):
        clear_canvas()
        grass.draw(400, 30)
        character.draw(300 + (r * math.cos(a)), 200 + (r * math.sin(a)))
        update_canvas()
        a += 1
        delay(0.1)

#사각형
j = 0
x = 100
y = 100
while 1:
    
    for i in range(40):
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, 90 + y)
        update_canvas()
        x += 4
        delay(0.01)
    for i in range(40):
            clear_canvas()
            grass.draw(400, 30)
            character.draw(x, 90 + y)
            update_canvas()
            y += 4
            delay(0.01)
    for i in range(40):
            clear_canvas()
            grass.draw(400, 30)
            character.draw(x, 90 + y)
            update_canvas()
            x -= 4
            delay(0.01)
    for i in range(40):
            clear_canvas()
            grass.draw(400, 30)
            character.draw(x, 90 + y)
            update_canvas()
            y -= 4
            delay(0.01)



close_canvas()