from matplotlib import pyplot as plt

def bresenham(x0, y0, x1, y1):
    xes = []
    yes = []

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x1 > x0 else -1
    sy = 1 if y1 > y0 else -1

    if dx >= dy:
        p = 2 * dy - dx
        x, y = x0, y0
        for _ in range(dx + 1):
            xes.append(x)
            yes.append(y)
            x += sx
            if p >= 0:
                y += sy
                p += 2 * dy - 2 * dx
            else:
                p += 2 * dy
    else:
        p = 2 * dx - dy
        x, y = x0, y0
        for _ in range(dy + 1):
            xes.append(x)
            yes.append(y)
            y += sy
            if p >= 0:
                x += sx
                p += 2 * dx - 2 * dy
            else:
                p += 2 * dx

    return xes, yes

x0 = int(input("Enter the values of x0: "))
y0 = int(input("Enter the values of y0: "))
x1 = int(input("Enter the values of x1: "))
y1 = int(input("Enter the values of y1: "))

xes, yes = bresenham(x0, y0, x1, y1)

plt.plot(xes, yes, marker="*")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Line from (x0, y0) to (x1, y1) using Bresenham's Algorithm")
plt.grid(True)
plt.show()