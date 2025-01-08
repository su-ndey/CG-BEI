import numpy as np
import matplotlib.pyplot as plt

def bresenham_line(x0, y0, x1, y1):
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

def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
    transformed_points = transformation_matrix @ points
    return transformed_points[0], transformed_points[1]

def plot_line_with_scaling_and_rotation():
    x0, y0, x1, y1 = map(int, input("Enter the values of x0, y0, x1, y1: ").split())

    x_orig, y_orig = bresenham_line(x0, y0, x1, y1)

    print("Choose the transformation:")
    print("1. Scaling")
    print("2. Rotation")
    transformation_choice = input("Enter 1 for Scaling or 2 for Rotation: ").strip()

    if transformation_choice == '1':
        scale_x = float(input("Enter the scaling factor for the X axis: "))
        scale_y = float(input("Enter the scaling factor for the Y axis: "))
        scaling_matrix = np.array([
            [scale_x, 0, 0],
            [0, scale_y, 0],
            [0, 0, 1]
        ])
        translation_to_origin_matrix = np.array([
            [1, 0, -x0],
            [0, 1, -y0],
            [0, 0, 1]
        ])
        translation_back_matrix = np.array([
            [1, 0, x0],
            [0, 1, y0],
            [0, 0, 1]
        ])

        composite_matrix = translation_back_matrix @ scaling_matrix @ translation_to_origin_matrix

    elif transformation_choice == '2':
        rotation_angle = float(input("Enter the rotation angle in degrees: "))
        theta = np.radians(rotation_angle)
        rotation_matrix = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])

        translation_to_origin_matrix = np.array([
            [1, 0, -x0],
            [0, 1, -y0],
            [0, 0, 1]
        ])

        translation_back_matrix = np.array([
            [1, 0, x0],
            [0, 1, y0],
            [0, 0, 1]
        ])

        composite_matrix = translation_back_matrix @ rotation_matrix @ translation_to_origin_matrix

    else:
        print("Invalid option, please enter '1' for Scaling or '2' for Rotation.")
        return

    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, composite_matrix)

    plt.figure(figsize=(8, 6))

    plt.plot(x_orig, y_orig, marker='*', color='blue', linestyle='-', label='Original Line')
    plt.plot(x_transformed, y_transformed, color='red', linestyle='--', label='Transformed Line')

    plt.title(f"Line with {'Scaling' if transformation_choice == '1' else 'Rotation'} Transformation")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)

    plt.show()

plot_line_with_scaling_and_rotation()
