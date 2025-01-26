import matplotlib.pyplot as plt
import numpy as np

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
    return xes, yes
def transformation(x1,y1,x2,y2):
    angle=int(input("rotation angle in degree: "))
    angle = angle/180.0 * 22/7 #conerting into radian
    sx = int(input("scaling of x axis: "))
    sy = int(input("scaling of y axis: "))
    x_coord, y_coord = blda(x1,y1,x2,y2)
    points = np.vstack([x_coord,y_coord,np.ones_like(x_coord)])
    transform= np.array([[1,0,-1],
                        [0,1,-1],
                        [0,0,1]]
    )
    inverse_transform=np.array([[1,0,1],
                               [0,1,1],
                               [0,0,1]]
    )
    scaling=np.array([[sx,0,0],
                     [0,sy,0],
                     [0,0,1]]
    )
    rotation= np.array(
        [
            [np.cos(angle),-np.sin(angle),0],
            [np.sin(angle),np.cos(angle),0],
            [0,0,1]
        ]
    )
    rotated= rotation @ points
    CM= inverse_transform @ scaling @ transform
    transformed_points= CM @ points
    x_transformed= transformed_points[0]
    y_transformed= transformed_points[1]
    x_r= rotated[0]
    y_r= rotated[1]
    plt.grid()
    plt.plot(x_coord, y_coord, marker='*',linestyle='-' , label="orignal line")
    plt.plot(x_transformed,y_transformed, marker='.',linestyle='none' , label="scaled line")
    plt.plot(x_r,y_r, marker='.',linestyle='--' ,label="rotated line")
    plt.show()
xo = int(input("xcoord of 1st point: "))
yo = int(input("ycoord of 1st point: "))
xi = int(input("xcoord of end point: "))
yi = int(input("ycoord of end point: "))
transformation(xo, yo, xi, yi)