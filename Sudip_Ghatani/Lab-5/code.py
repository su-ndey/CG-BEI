import numpy as np
import os

from matplotlib import pyplot as plt

def bresenham(x0, y0, x1, y1):
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

def apply_2d_transition(x_co,y_co,transform):
    points = np.vstack([x_co,y_co,np.ones_like(x_co)])
    transform = transform @ points   
    return transform[0],transform[1]

def plot_transform():
    x0 = int(input("Enter the values of x0: "))
    y0 = int(input("Enter the values of y0: "))
    x1 = int(input("Enter the values of x1: "))
    y1 = int(input("Enter the values of y1: "))
    xes, yes = bresenham(x0, y0, x1, y1)
    scale_x = int(input("Enter the value for scaling in x: "))
    scale_y = int(input("Enter the value for scaling in y: "))
    translate_x = int(input("Enter the value for translating in x: "))
    translate_y = int(input("Enter the value for translating in x: "))
    scaling_matrix = np.array([
        [scale_x,0,0],
        [0,scale_y,0],
        [0,0,1],   
    ])
    translate_matrix = np.array([
        [1,0,translate_x],
        [0,1,translate_y],
        [0,0,1],   
    ])
    translate_matrix_inverse = np.array([
        [1,0,-translate_x],
        [0,1,-translate_y],
        [0,0,1],   
    ])
    
    CM = translate_matrix @ scaling_matrix @ translate_matrix_inverse
    
    x_t,y_t = apply_2d_transition(xes,yes,CM)
    
    plt.figure(figsize = (8,6))
    
    plt.plot(xes,yes,marker = '*',color = 'green', linestyle = '-', label = 'Original line')
    
    plt.plot(x_t,y_t,marker = 'o',color = 'blue', linestyle = '--', label = 'Transformed line')
    
    plt.title("Bresenham LIne with 2D Transformations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()
    
def plot_rotation():
    x0 = int(input("Enter the values of x0: "))
    y0 = int(input("Enter the values of y0: "))
    x1 = int(input("Enter the values of x1: "))
    y1 = int(input("Enter the values of y1: "))
    xes, yes = bresenham(x0, y0, x1, y1)
    degree = int(input("Enter the degree of rotation: "))
    theta = degree * np.pi/180
    translate_x = int(input("Enter the value for translating in x: "))
    translate_y = int(input("Enter the value for translating in x: "))
    rotation_matrix = np.array([
        [np.cos(theta),-np.sin(theta),0],
        [np.sin(theta),np.cos(theta),0],
        [0,0,1],   
    ])
    translate_matrix = np.array([
        [1,0,translate_x],
        [0,1,translate_y],
        [0,0,1],   
    ])
    translate_matrix_inverse = np.array([
        [1,0,-translate_x],
        [0,1,-translate_y],
        [0,0,1],   
    ])
    
    CM = translate_matrix @ rotation_matrix @ translate_matrix_inverse
    
    x_t,y_t = apply_2d_transition(xes,yes,CM)
    
    plt.figure(figsize = (10,10))
    
    plt.plot(xes,yes,marker = '*',color = 'green', linestyle = '-', label = 'Original line')
    
    plt.plot(x_t,y_t,marker = 'o',color = 'blue', linestyle = '--', label = 'Transformed line')
    
    plt.title("Bresenham LIne with 2D Transformations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()

print("1.Transformation\n2.Rotation")
choice = int(input("Enter your choice: "))
os.system('cls')
if choice == 1:
    plot_transform()
if choice == 2:
    plot_rotation()
else:
    print("wrong choice")
