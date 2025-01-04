import matplotlib.pyplot as plt 
def dda(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    steps=max(abs(dy),abs(dy))
    x_increment=dx/steps
    y_increment=dy/steps
    x=x1
    y=y1
    xes=[]
    yes=[]
    for i in range(steps):
        xes.append(round(x))
        yes.append(round(y))
        x=x+x_increment
        y=y+y_increment
    plt.grid()
    plt.plot(xes,yes)
    plt.show()
xo=int(input("xcoord of 1st point"))
yo=int(input("ycoord of 1st point"))
xi=int(input("xcoord of end point"))
yi=int(input("xcoord of end point"))
dda(xo,yo,xi,yi)
    