import numpy as np
import matplotlib.pyplot as plt
def bresenham(x1, y1, x2, y2):
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
def apply_2d_transformation(x_coords,y_coords,transformation_matrix):
    points=np.stack([x_coords,y_coords,np.ones_like(x_coords)])
    transformed_points=transformation_matrix@points
    return transformed_points[0],transformed_points[1]
def plot_line_with_transformations(x0,y0,x1,y1):
    x_org,y_org=bresenham(x0,y0,x1,y1)
    scaling_matrix=np.array([
        [2,0,0],
        [0,0.5,0],
        [0,0,1]
    ])
    translation_matrix=np.array([
        [1,0,3],
        [0,1,2],
        [0,0,1]
    ])
    transformation_matrix=np.array([
        [1,0,-3],
        [0,1,-2],
        [0,0,1]
    ])
    composite_matrix=translation_matrix@scaling_matrix@transformation_matrix
    x_transformed,y_transformed=apply_2d_transformation(x_org,y_org,composite_matrix)
    plt.figure(figsize=(8, 6))
    plt.plot(x_org, y_org, marker='*', color='blue', linestyle='-', label='Original Line')
    plt.plot(x_transformed, y_transformed, color='red', linestyle='--', label='Transformed Line')
    
    plt.title("Bresenham Line with 2D Transformations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)

    plt.show()

plot_line_with_transformations(2, 3, 10, 8)



