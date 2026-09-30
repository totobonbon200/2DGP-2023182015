# Animation Viewer Plan

## Goal

Build `animation_viewer.py` with `pico2d` and `spelunky_animation_sheet.png`. Show one animation group at a time in the center of the canvas, enlarge the character to a useful on-screen size, and keep cycling through all 12 groups. Each group plays five times, pauses for one second, then advances. Number keys select a group directly.

## Sprite Sheet Mapping

- The source image is 2048 x 2048 pixels.
- Use the first 12 horizontal bands in order, starting with the top band. The measured grid unit is 128 x 128 pixels. Represent every frame as an explicit `(x, y, width, height)` rectangle.
- Skip transparent cells. The occupied source columns are: row 1 `0-15`; row 2 `0-11, 13-14`; row 3 `0-14`; row 4 `0-14`; row 5 `0-10, 12-15`; row 6 `0-14`; row 7 `0-11, 13-14`; row 8 `0-14`; row 9 `0-14`; row 10 `0-15`; row 11 `0-15`; row 12 `0-10`.
- Group 1: walking, followed by the swimming frames on the right.
- Group 2: crouching and moving forward while crouched.
- Group 3: taking damage and falling; use only frames 1 through 4.
- Group 4: columns 0-10 wobble at the edge; the rightmost four occupied frames (columns 11-14) hang from a ledge.
- Group 5: throwing an object.
- Group 6: entering and exiting a door.
- Group 7: ladder movement on the left, pushing on the right.
- Group 8: columns 0-9 climb a rope; use the rightmost five occupied frames (columns 10-14) for crouching and standing.
- Group 9: looking up, selected with the up-arrow key.
- Group 10: jumping, excluding rope frames.
- Group 11: ghost movement and shooting after death.
- Group 12: falling between platforms.

## Controls

- Top-row `1` through `9` select groups 1 through 9.
- Top-row `0` selects group 10.
- Numpad `1` and `2` select groups 11 and 12.
- Up arrow selects the look-up pose/group (group 9).
- Escape or closing the window exits cleanly.

## Implementation Steps

1. Commit this plan and record the source asset path.
2. Start the `pico2d` viewer module.
3. Define the canvas dimensions and frame rate.
4. Load the Spelunky sprite sheet from the script directory.
5. Define named frame rectangles and animation groups.
6. Add the 12 group labels and playback order.
7. Define the number-key to group mapping.
8. Initialize selection, frame, repeat, and pause state.
9. Poll `pico2d` window events once per loop.
10. Handle window-close and Escape events.
11. Advance the selected group's frame cursor.
12. Keep frame timing independent of canvas redraw details.
13. Count completed group repetitions.
14. Pause for one second after five repetitions.
15. Advance to the next group after its pause.
16. Wrap the automatic sequence from group 12 to group 1.
17. Center the character on the canvas.
18. Calculate a display size that occupies at least half the canvas height.
19. Draw the current source rectangle with `pico2d` clipping.
20. Clear and update the canvas on every frame.
21. Reset playback state when a number key selects another group.
22. Make manual selection continue through the same automatic order.
23. Close the canvas on normal exit.
24. Check all source rectangles and special frame-count limits.
25. Run syntax and focused runtime checks, then review the final diff.

## Verification

- Pylance resolves `pico2d` in the selected Python 3.13 environment.
- Syntax validation passes for `animation_viewer.py`.
- The sheet loads from the script's own directory, independent of the shell working directory.
- Per-group frame counts are 16, 14, 4, 15, 15, 15, 14, 15, 15, 16, 16, and 11; every mapped frame rectangle stays inside the 2048 x 2048 source image.
- Number-key mapping covers all 12 groups; group 3 has four frames; group 4 reserves its rightmost four frames; group 8 reserves its rightmost five frames.
- Playback advances after five loops, waits one second, and wraps after group 12.