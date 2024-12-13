import matplotlib.pyplot as plt


def plot_points(xes,yes,x,y,xc,yc):
    xes.append(x+xc)
    yes.append(y+yc)

    xes.append(-x+xc)
    yes.append(y+yc)

    xes.append(-x+xc)
    yes.append(-y+yc)

    xes.append(x+xc)
    yes.append(-y+yc)

    xes.append(y+xc)
    yes.append(x+yc)

    xes.append(-y+xc)
    yes.append(x+yc)

    xes.append(y+xc)
    yes.append(-x+yc)

    xes.append(-y+xc)
    yes.append(-x+yc)
    
def midpoint_circle(r,xc,yc):
    x=0
    y=r
    p=1-r
    xes=[]
    yes=[]
    plot_points(xes,yes,x,y,xc,yc)

    while x<y:
        x = x+1
        if(p<0):
            p=p+2*x+1
        else:
            y=y-1
            p=p+2*(x-y)+1
        plot_points(xes,yes,x,y,xc,yc)
    plt.scatter(xes,yes)
    plt.show()


r = int(input("Enter the radius of the circle: "))
xc = int(input("Enter the x-coord for center of circle: "))
yc = int(input("Enter the y-coord for center of circle: "))
midpoint_circle(r,xc,yc)




