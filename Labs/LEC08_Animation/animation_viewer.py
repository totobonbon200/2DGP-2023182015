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


def main():
	open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
	sprite_sheet = load_image(str(ASSET_PATH))
	close_canvas()


if __name__ == '__main__':
	main()
