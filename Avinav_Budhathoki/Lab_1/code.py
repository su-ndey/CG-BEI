from matplotlib import pyplot as plt

# DDA Algorithm Function
def dda_line(x0, y0, x1, y1):
    delX = x1 - x0
    delY = y1 - y0
    steps = max(abs(delX), abs(delY))  # Determine the number of steps
    xIncrement = delX / steps         # Calculate x increment
    yIncrement = delY / steps         # Calculate y increment

    x = x0
    y = y0
    xes = []  # List to store x coordinates
    yes = []  # List to store y coordinates

    for i in range(steps + 1):  # Generate points for the line
        xes.append(round(x))  # Append rounded x value
        yes.append(round(y))  # Append rounded y value
        x += xIncrement       # Increment x
        y += yIncrement       # Increment y

    return xes, yes

# Input values for the line endpoints
x0, y0, x1, y1 = map(int, input("Enter the values of x0, y0, x1, y1: ").split())

# Calculate the line points using DDA algorithm
xes, yes = dda_line(x0, y0, x1, y1)

# Plot the calculated points
plt.plot(xes, yes, marker="o")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title(f"Line from ({x0}, {y0}) to ({x1}, {y1}) using DDA")
plt.grid(True)
plt.show()
