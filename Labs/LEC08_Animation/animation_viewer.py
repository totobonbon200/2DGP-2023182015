from pathlib import Path
from time import monotonic

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_SIZE = 128
FRAME_DURATION = 0.1
REPEAT_COUNT = 5
PAUSE_DURATION = 1.0
ASSET_PATH = Path(__file__).with_name('spelunky_animation_sheet.png')


def frame_rect(row, column, width=FRAME_SIZE, height=FRAME_SIZE):
	return column * FRAME_SIZE, row * FRAME_SIZE, width, height


def row_frames(row, columns):
	return [frame_rect(row, column) for column in columns]


ANIMATIONS = [
	{'name': '걷기 / 수영', 'frames': row_frames(0, range(16))},
	{'name': '숙이기 / 숙여서 이동', 'frames': row_frames(1, range(16))},
	{'name': '피해 / 쓰러지기', 'frames': row_frames(2, range(4))},
	{'name': '절벽 비틀거림 / 매달리기', 'frames': row_frames(3, range(16))},
	{'name': '던지기', 'frames': row_frames(4, range(16))},
]


def main():
	open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
	sprite_sheet = load_image(str(ASSET_PATH))
	close_canvas()


if __name__ == '__main__':
	main()
