import numpy as np
import matplotlib.pyplot as plt

def bresenham_line(x0, y0, x1, y1):
    """Generates points for a line using Bresenham's Algorithm."""
    xes, yes = [], []
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx, sy = (1 if x1 > x0 else -1), (1 if y1 > y0 else -1)

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

def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    """Applies a 2D transformation matrix to a set of points."""
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])  # Homogeneous coordinates
    transformed_points = transformation_matrix @ points  # Matrix multiplication
    return transformed_points[0], transformed_points[1]

def apply_scaling(x_coords, y_coords, scale_x, scale_y):
    """Scales the points by scale_x and scale_y."""
    x_scaled = [x * scale_x for x in x_coords]
    y_scaled = [y * scale_y for y in y_coords]
    return x_scaled, y_scaled

def plot_fixed_point_rotation():
    """Plots the original and rotated line using fixed-point rotation."""
    # Input original line endpoints
    x0, y0, x1, y1 = map(int, input("Enter the values of x0, y0, x1, y1: ").split())

    # Generate points for the original line using Bresenham's algorithm
    x_orig, y_orig = bresenham_line(x0, y0, x1, y1)

    # Input rotation angle and convert to radians
    theta = float(input("Enter rotation angle in degrees: "))
    theta = np.radians(theta)

    # Use the first point (x0, y0) as the fixed point for rotation
    fx, fy = x0, y0

    # Create the translation matrix to move the fixed point to the origin
    translation_to_origin = np.array([
        [1, 0, -fx],
        [0, 1, -fy],
        [0, 0, 1]
    ])

    # Create the rotation matrix for the given angle
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

    # Create the inverse translation matrix to move the points back to their original position
    inverse_translation = np.array([
        [1, 0, fx],
        [0, 1, fy],
        [0, 0, 1]
    ])

    # Composite transformation matrix: first move to origin, then rotate, and finally move back
    composite_matrix = inverse_translation @ rotation_matrix @ translation_to_origin

    # Apply the transformation (rotation) to the original points
    x_rotated, y_rotated = apply_2d_transformation(x_orig, y_orig, composite_matrix)

    # Plot original and rotated lines
    plt.figure(figsize=(8, 6))
    plt.plot(x_orig, y_orig, marker='o', color='blue', linestyle='-', label='Original Line')
    plt.plot(x_rotated, y_rotated, color='green', linestyle='--', label='Rotated Line')
    plt.title("Bresenham Line with Fixed-Point Rotation")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_scaled_line():
    """Plots the original and scaled line."""
    # Input original line endpoints
    x0, y0, x1, y1 = map(int, input("Enter the values of x0, y0, x1, y1: ").split())

    # Generate points for the original line using Bresenham's algorithm
    x_orig, y_orig = bresenham_line(x0, y0, x1, y1)

    # Input scaling factors for the x and y axes
    scale_x = float(input("Enter scaling factor for x-axis: "))
    scale_y = float(input("Enter scaling factor for y-axis: "))

    # Apply scaling transformation to the original points
    x_scaled, y_scaled = apply_scaling(x_orig, y_orig, scale_x, scale_y)

    # Plot original and scaled lines
    plt.figure(figsize=(8, 6))
    plt.plot(x_orig, y_orig, marker='o', color='blue', linestyle='-', label='Original Line')
    plt.plot(x_scaled, y_scaled, color='red', linestyle='--', label='Scaled Line')
    plt.title("Bresenham Line with Scaling")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()

print("Choose an operation:")
print("1. Scaling")
print("2. Fixed-Point Rotation")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    plot_scaled_line()
elif choice == 2:
    plot_fixed_point_rotation()
else:
    print("Invalid choice.")
