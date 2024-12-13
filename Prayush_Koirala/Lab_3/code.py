import matplotlib.pyplot as plt

def circle(r, x1, y1):
    x = 0
    y = r
    p = 1 - r
    xes = []
    yes = []
    while x <= y:
        xes.extend([x + x1, x + x1, y + x1, -y + x1, -x + x1, -x + x1, -y + x1, y + x1])
        yes.extend([y + y1, -y + y1, -x + y1, -x + y1, -y + y1, y + y1, x + y1, x + y1])
        x = x + 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y = y - 1
            p = p + 2 * (x - y) + 1
    plt.grid()
    plt.scatter(xes, yes, marker='o')
    plt.show()

r = int(input("Enter radius: "))
x1 = int(input("Enter x coordinate of center: "))
y1 = int(input("Enter y coordinate of center: "))
circle(r, x1, y1)