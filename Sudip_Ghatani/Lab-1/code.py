from matplotlib import pyplot as plt

def dda_line(x0, y0, x1, y1):
    X0 = x1 - x0
    Y0 = y1 - y0
    steps = max(abs(X0), abs(Y0))
    xInc = X0 / steps
    yInc = Y0 / steps

    x = x0
    y = y0
    xes = []
    yes = []

    for i in range(steps + 1):
        xes.append(round(x))
        yes.append(round(y))
        x += xInc
        y += yInc

    return xes, yes

x0, y0, x1, y1 = map(int, input("Enter the values of x0, y0, x1, y1: ").split())
xes, yes = dda_line(x0, y0, x1, y1)

plt.plot(xes, yes, marker="o")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Line from (x0, y0) to (x1, y1)")
plt.grid(True)
plt.show()