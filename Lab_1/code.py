from matplotlib import pyplot as plt

def dda_line(x0, y0, x1, y1):
    delX = x1 - x0
    delY = y1 - y0
    steps = max(abs(delX), abs(delY))
    xIncrement = delX / steps
    yIncrement = delY / steps

    x = x0
    y = y0
    xes = []
    yes = []

    for i in range(steps + 1):
        xes.append(round(x))
        yes.append(round(y))
        x += xIncrement
        y += yIncrement

    return xes, yes

x0, y0, x1, y1 = map(int, input("Enter the values of x0, y0, x1, y1: ").split())
xes, yes = dda_line(x0, y0, x1, y1)

plt.plot(xes, yes, marker="o")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Line from (x0, y0) to (x1, y1)")
plt.grid(True)
plt.show()
