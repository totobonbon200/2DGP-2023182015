from pathlib import Path
from time import monotonic

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_SIZE = 128
SHEET_HEIGHT = 2048
FRAME_DURATION = 0.1
REPEAT_COUNT = 5
PAUSE_DURATION = 1.0
ASSET_PATH = Path(__file__).with_name('spelunky_animation_sheet.png')


def frame_rect(row, column, width=FRAME_SIZE, height=FRAME_SIZE):
	bottom = SHEET_HEIGHT - (row + 1) * FRAME_SIZE
	return column * FRAME_SIZE, bottom, width, height


def row_frames(row, columns):
	return [frame_rect(row, column) for column in columns]


LEDGE_WOBBLE_FRAMES = row_frames(3, range(12))
LEDGE_HANG_FRAMES = row_frames(3, range(12, 16))
ROPE_FRAMES = row_frames(7, range(11))
CROUCH_STAND_FRAMES = row_frames(7, range(11, 16))


ANIMATIONS = [
	{'name': '걷기 / 수영', 'frames': row_frames(0, range(16))},
	{'name': '숙이기 / 숙여서 이동', 'frames': row_frames(1, range(16))},
	{'name': '피해 / 쓰러지기', 'frames': row_frames(2, range(4))},
	{'name': '절벽 비틀거림 / 매달리기', 'frames': LEDGE_WOBBLE_FRAMES + LEDGE_HANG_FRAMES},
	{'name': '던지기', 'frames': row_frames(4, range(16))},
	{'name': '문 들어가기 / 나오기', 'frames': row_frames(5, range(16))},
	{'name': '사다리 / 밀기', 'frames': row_frames(6, range(16))},
	{'name': '밧줄 / 숙였다 일어서기', 'frames': ROPE_FRAMES + CROUCH_STAND_FRAMES},
	{'name': '위 보기', 'frames': row_frames(8, range(16))},
	{'name': '점프', 'frames': row_frames(9, range(16))},
	{'name': '유령 이동 / 발사', 'frames': row_frames(10, range(16))},
	{'name': '낙하', 'frames': row_frames(11, range(16))},
]

KEY_TO_ANIMATION = {
	SDLK_1: 0,
	SDLK_2: 1,
	SDLK_3: 2,
	SDLK_4: 3,
	SDLK_5: 4,
	SDLK_6: 5,
	SDLK_7: 6,
	SDLK_8: 7,
	SDLK_9: 8,
	SDLK_0: 9,
	SDLK_KP_1: 10,
	SDLK_KP_2: 11,
}


def reset_playback_state(animation_index, now):
	return {
		'animation_index': animation_index,
		'frame_index': 0,
		'repeat_count': 0,
		'last_frame_time': now,
		'pause_until': 0.0,
	}


def handle_keydown(key, state, now):
	if key == SDLK_ESCAPE:
		return False, state

	animation_index = KEY_TO_ANIMATION.get(key)
	if key == SDLK_UP:
		animation_index = 8
	if animation_index is not None:
		state = reset_playback_state(animation_index, now)
	return True, state


def main():
	open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
	sprite_sheet = load_image(str(ASSET_PATH))
	close_canvas()


if __name__ == '__main__':
	main()
