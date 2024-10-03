from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
boy = load_image('animation_sheet.png')

def line_rendering(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    a = (y2-y1)/(x2-x1)
    b = y1 - x1 * a
    for x in range(x1, x2+1, 10):
        clear_canvas()
        y = a * x + b
        boy.clip_draw(100, 100, 100, 100, x, y)
        update_canvas()
        delay(0.02)

line_rendering((10, 10), (300, 300))