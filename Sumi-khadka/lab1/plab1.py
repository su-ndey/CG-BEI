import matplotlib.pyplot as plt
def dda(x0,y0,x1,y1):


    dx = x1-x0
    dy = y1-y0
    steps = max(abs(dx),abs(dy))
    x_increment = dx/steps
    y_increment = dy/steps
    x = x0
    y = y0
    xes = []
    yes = []
    for i in range(steps):
        xes.append(x)
        yes.append(y)
        x = x+x_increment  
        y = y+y_increment 

    plt.plot(xes,yes,marker='*')
    plt.show()

x0 = int(input("enter the point x0"))
x1 = int(input("enter the point x1"))
y0 = int(input ("enter the point y0"))
y1 = int(input("enter the point y1"))
dda(x0,x1,y0,y1)
