from pathlib import Path
from time import monotonic

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
SPRITE_PATH = Path(__file__).with_name('sonic-sprite.png')
FRAME_DELAY = 0.18
MOVE_SPEED = 240
DISPLAY_SCALE = 2.6
GRID_ROWS = 12
GRID_COLS = 12
SHEET_WIDTH = 399
SHEET_HEIGHT = 525
CELL_WIDTH = SHEET_WIDTH // GRID_COLS
CELL_HEIGHT = 40

VISIBLE_COLUMNS = {
    2: range(12),
    3: range(9),
    4: range(10),
    5: range(7),
    6: range(8),
    7: range(8),
    8: range(9),
    9: range(9),
    10: range(6),
    11: range(9),
}

ANIMATION_NAMES = [
    'idle',
    'run',
    'jump',
    'spin',
    'slide',
    'hurt',
    'crouch',
    'climb',
    'hang',
    'die',
]


def frame_rect(row, col):
    left = col * CELL_WIDTH
    bottom = SHEET_HEIGHT - (row + 1) * CELL_HEIGHT
    return left, bottom, CELL_WIDTH, CELL_HEIGHT


def build_animation(row_index):
    row = row_index + 2
    columns = VISIBLE_COLUMNS.get(row, range(1))
    return [frame_rect(row, col) for col in columns]


ANIMATIONS = [
    {'name': 'idle', 'frames': build_animation(0)},
    {'name': 'run', 'frames': build_animation(1)},
    {'name': 'jump', 'frames': build_animation(2)},
    {'name': 'spin', 'frames': build_animation(3)},
    {'name': 'slide', 'frames': build_animation(4)},
    {'name': 'hurt', 'frames': build_animation(5)},
    {'name': 'crouch', 'frames': build_animation(6)},
    {'name': 'climb', 'frames': build_animation(7)},
    {'name': 'hang', 'frames': build_animation(8)},
    {'name': 'die', 'frames': build_animation(9)},
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
}


def reset_state(animation_index, now):
    return {
        'animation_index': animation_index,
        'frame_index': 0,
        'last_frame_time': now,
        'last_update_time': now,
        'x': CANVAS_WIDTH // 2,
        'moving': False,
    }


def handle_keydown(key, state, now):
    if key == SDLK_ESCAPE:
        return False, state

    if key == SDLK_1:
        state = reset_state(0, now)
        state['x'] = 0
        state['moving'] = True
        return True, state

    animation_index = KEY_TO_ANIMATION.get(key)
    if animation_index is not None:
        state = reset_state(animation_index, now)

    return True, state


def update_animation(state, now):
    elapsed = now - state['last_update_time']
    state['last_update_time'] = now
    if state['moving']:
        state['x'] = min(CANVAS_WIDTH, state['x'] + MOVE_SPEED * elapsed)
        if state['x'] == CANVAS_WIDTH:
            state['moving'] = False

    if now - state['last_frame_time'] < FRAME_DELAY:
        return state

    state['last_frame_time'] = now
    animation = ANIMATIONS[state['animation_index']]
    state['frame_index'] = (state['frame_index'] + 1) % len(animation['frames'])
    return state


def draw_frame(sprite_sheet, state):
    clear_canvas()
    animation = ANIMATIONS[state['animation_index']]
    left, bottom, width, height = animation['frames'][state['frame_index']]
    draw_size = max(60, min(CANVAS_WIDTH, CANVAS_HEIGHT) * 0.45)

    sprite_sheet.clip_draw(
        left,
        bottom,
        width,
        height,
        state['x'],
        CANVAS_HEIGHT // 2,
        draw_size,
        draw_size * 1.2,
    )
    update_canvas()


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    sprite_sheet = load_image(str(SPRITE_PATH))
    state = reset_state(0, monotonic())
    running = True

    try:
        while running:
            now = monotonic()
            for event in get_events():
                if event.type == SDL_QUIT:
                    running = False
                elif event.type == SDL_KEYDOWN:
                    running, state = handle_keydown(event.key, state, now)

            if running:
                state = update_animation(state, now)
                draw_frame(sprite_sheet, state)
                delay(1 / 60)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
