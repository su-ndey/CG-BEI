import matplotlib.pyplot as plt

def midpoint_ellipse(rx, ry, xc, yc):
    # Initialize variables
    x = 0
    y = ry
    rx2 = rx**2
    ry2 = ry**2
    two_rx2 = 2 * rx2
    two_ry2 = 2 * ry2

    # Region 1
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
    dx = two_ry2 * x
    dy = two_rx2 * y

    points = []

    while dx < dy:
        # Plot points for all four quadrants
        points.extend([
            (x + xc, y + yc), (-x + xc, y + yc),
            (x + xc, -y + yc), (-x + xc, -y + yc)
        ])

        # Update x and decision parameter
        if p1 < 0:
            x += 1
            dx += two_ry2
            p1 += dx + ry2
        else:
            x += 1
            y -= 1
            dx += two_ry2
            dy -= two_rx2
            p1 += dx - dy + ry2

    # Region 2
    p2 = ry2 * (x + 0.5)**2 + rx2 * (y - 1)**2 - rx2 * ry2

    while y >= 0:
        # Plot points for all four quadrants
        points.extend([
            (x + xc, y + yc), (-x + xc, y + yc),
            (x + xc, -y + yc), (-x + xc, -y + yc)
        ])

        # Update y and decision parameter
        if p2 > 0:
            y -= 1
            dy -= two_rx2
            p2 += rx2 - dy
        else:
            y -= 1
            x += 1
            dx += two_ry2
            dy -= two_rx2
            p2 += dx - dy + rx2

    # Plot all points
    plot_points(points)

def plot_points(points):
    for (x, y) in points:
        plt.plot(x, y, 'ro')  # 'ro' means red dot

# Main function to call the algorithm
rx = int(input("Enter the radius of the ellipse for x-axis: "))
ry = int(input("Enter the radius of the ellipse for y-axis: "))
xc = int(input("Enter the x-coordinate of the ellipse center: "))
yc = int(input("Enter the y-coordinate of the ellipse center: "))

midpoint_ellipse(rx, ry, xc, yc)

plt.title("Midpoint Ellipse Drawing Algorithm")
plt.xlabel("x-coordinate")
plt.ylabel("y-coordinate")
plt.axis('equal')  # Equal scaling for x and y axes
plt.grid()
plt.show()