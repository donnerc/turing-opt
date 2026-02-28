from gpanel import *

MAX_X = 2
MAX_Y = 2
n = 200
SCREEN_W = 2 * MAX_X * n
SCREEN_H = 2 * MAX_Y * n

makeGPanel(Size(SCREEN_W, SCREEN_H))
#window(-SCREEN_W // 2, SCREEN_W // 2, SCREEN_H, 0)    # y axis downwards
bm = GBitmap(SCREEN_W, SCREEN_H)

black = makeColor(0, 0, 0)
blue = makeColor(0, 0, 255)

def frange(lbound, ubound, nbsteps):
    step = (ubound - lbound) / nbsteps
    return [lbound + step * i for i in range(nbsteps + 1)]


def sequence(c, z=0):
    while True:
        yield z
        z = z ** 2 + c
    
def mandelbrot(candidate):
    return sequence(z=0, c=candidate)
    
def is_stable(c, num_iterations):
    z = 0
    nb_iterations = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
        nb_iterations += 1
        if abs(z) > 2:
            return nb_iterations
    return 0

def tr(x, y, factor=1):
    '''
    >>> tr(0, 0)
    (200, 200)
    >>> tr(2, 0)
    (400, 200)
    >>> tr(-2, 0)
    (0, 200)
    >>> tr(0, 2)
    (200, 0)
    >>> tr(0, -2)
    (200, 400)
    '''
    panel_x = int((x + 2) * n)
    panel_y = int((-y + 2) * n)
    return panel_x, panel_y

def draw(scale=1, cx=0, cy=0):
    d = SCREEN_W / scale / n / 3
    
    max_iter = 200
    colors = [makeColor(50, 40 + i, 40 + i) for i in range(max_iter)]
    
    for y in frange(cy-d, cy+d, SCREEN_H):    
        for x in frange(cx-d, cx+d, SCREEN_W):
            c = x + y * 1j
            nb_iters = is_stable(c, max_iter)
            color = colors[nb_iters-1] if nb_iters else black
            px, py = tr(scale* (x - cx), scale * (y-cy))
            #print(px, py)
            try:
                bm.setPixelColor(px, py, color)
            except:
                pass
        
    image(bm, 0, 0)


# tester avec différentes valeurs de scale 1 .. 400
scale = 1
cx = -0.95
cy = 0.25
draw(scale, cx, cy)

