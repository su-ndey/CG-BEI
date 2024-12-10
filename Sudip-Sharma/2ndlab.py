import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    """
    Implements the Bresenham's Line Algorithm (DDA) to draw a line between two points.

    Args:
        x1 (int): X-coordinate of the starting point.
        y1 (int): Y-coordinate of the starting point.
        x2 (int): X-coordinate of the ending point.
        y2 (int): Y-coordinate of the ending point.

    Returns:
        None
    """

    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))  # Correctly calculate the number of steps

    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1
    xes = []
    yes = []

    for _ in range(steps):  # Use a throwaway variable for loop iteration
        xes.append(round(x))
        yes.append(round(y))
        x += x_increment
        y += y_increment

    plt.grid(True)  # Set grid visibility to True
    plt.plot(xes, yes)
    plt.xlabel("X-axis")  # Add axis labels for clarity
    plt.ylabel("Y-axis")
    plt.title("Line using DDA Algorithm")  # Add a title
    plt.show()

# Get input coordinates
xo = int(input("X-coordinate of the 1st point: "))
yo = int(input("Y-coordinate of the 1st point: "))
xi = int(input("X-coordinate of the end point: "))
yi = int(input("Y-coordinate of the end point: "))

dda(xo, yo, xi, yi)