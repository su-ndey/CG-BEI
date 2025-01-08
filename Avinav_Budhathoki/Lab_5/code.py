import numpy as np
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

    return xes,yes

def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    points=np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
    transformed_points = transformation_matrix @ points
    return transformed_points[0], transformed_points[1]

def plot_line_with_transformations(x1, y1, x2, y2):
    x_orig,y_orig=blda(x1, y1, x2, y2)
    scaling_matrix=np.array([
        [2,0,0],
        [0,0.5,0],
        [0,0,1]
    ])
    translation_matrix = np.array([
        [1, 0, 2],
        [0, 1, 3],
        [0, 0, 1]
    ])
    transform_matrix = np.array([
        [1, 0, -2],
        [0, 1, -3],
        [0, 0, 1]
    ])

    theta =  np.pi / 4
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

    composite_matrix = translation_matrix @ rotation_matrix @ transform_matrix
    x_transformed,y_transformed = apply_2d_transformation(x_orig,y_orig,composite_matrix)
    plt.figure(figsize=(8, 6))
    plt.plot(x_orig, y_orig, marker='*', color='blue', linestyle='-', label='Original Line')
    plt.plot(x_transformed, y_transformed, color='red', linestyle='--', label='Transformed Line')
    
    plt.title("Bresenham Line with 2D Transformations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)


    plt.show()

plot_line_with_transformations(5,5,7,7)