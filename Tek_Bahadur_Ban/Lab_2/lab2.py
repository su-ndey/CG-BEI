import matplotlib.pyplot as plt

def blda(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    x = x1
    y = y1
    xes = []
    yes = []
    if dx >= dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            xes.append(x)
            yes.append(y)
            if p >= 0:
                y = y + sy
                p = p + 2 * (dy - dx)
            else:
                p = p + 2 * dy
            x = x + sx
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            xes.append(x)
            yes.append(y)
            if p >= 0:
                x = x + sx
                p = p + 2 * (dx - dy)
            else:
                p = p + 2 * dx
            y = y + sy
    plt.grid()
    plt.plot(xes, yes, marker='o')
    plt.show()

xo = int(input("xcoord of 1st point: "))
yo = int(input("ycoord of 1st point: "))
xi = int(input("xcoord of end point: "))
yi = int(input("ycoord of end point: "))
blda(xo, yo, xi, yi)