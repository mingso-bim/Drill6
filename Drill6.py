from pico2d import *
import random

open_canvas()
background = load_image('TUK_GROUND.png')
boy = load_image('animation_sheet.png')

def line_move(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    a = (y2-y1)/(x2-x1)
    b = y1 - x1 * a

    if x1 > x2:
        step = -10
    else:
        step = 10

    for x in range(x1, x2+1, step):
        clear_canvas()
        y = a * x + b
        background.draw(400, 300)
        boy.clip_draw(100, 100, 100, 100, x, y)
        update_canvas()
        delay(0.02)

old_point = [400, 300]
target_point = [0, 0]

while True:
    target_point[0] = random.randint(50, 750)
    target_point[1] = random.randint(50, 550)

    line_move(old_point, target_point)
    old_point = target_point.copy()