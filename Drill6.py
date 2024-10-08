from pico2d import *
import random

open_canvas()
background = load_image('TUK_GROUND.png')
boy = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def line_move(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    a = (y2-y1)/(x2-x1)
    b = y1 - x1 * a

    if x1 > x2:
        step = -10
    else:
        step = 10
    frame = 0

    for x in range(x1, x2+1, step):
        clear_canvas()
        y = a * x + b
        background.draw(400, 300)
        frame = (frame + 1) % 8
        if x1 > x2:
            boy.clip_draw(frame * 100, 0, 100, 100, x, y)
        else:
            boy.clip_draw(frame * 100, 100, 100, 100, x, y)
        hand.draw(x2, y2)
        update_canvas()
        delay(0.02)

old_point = [400, 300]
target_point = [0, 0]

while True:
    target_point[0] = random.randint(50, 750)
    target_point[1] = random.randint(50, 550)

    line_move(old_point, target_point)
    old_point = target_point.copy()