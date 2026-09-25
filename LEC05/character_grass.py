#필요한 라이브러리 함수
from pico2d import *
import math

# (800, 600) 캔버스 실행
open_canvas(800, 600)

# 실행에 필요한 이미지 로드
grass = load_image('grass.png')
character = load_image('character.png')

# 확인용 코드
grass.draw(400, 30)
character.draw(400, 90)
delay(10)

# 캔버스 종료
close_canvas()