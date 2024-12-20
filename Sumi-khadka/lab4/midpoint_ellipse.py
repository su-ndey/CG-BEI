import matplotlib.pyplot as plt
def midpoint_ellipse(rx,ry,xc,yc):
    x=0
    y=ry
    p1=ry**2-(rx*rx*ry)+(0.25*rx*rx)
    xes=[]
    yes=[]
    while 2*ry*ry*x<=2*rx*rx*y:
        plot_points(xes,yes,x,y,xc,yc)
        if p1<0:
            x+=1
            p1+=2*ry*ry*x+ry*ry
        else:
            x+=1
            y-=1
            p1+=2*ry*ry*x-2*rx*ry*y+ry*ry
        plot_points(xes,yes,x,y,xc,yc)
    p2=(ry*ry*(x+0.5)**2)+(rx*rx*(y-1)**2)-(rx*rx*ry*ry)
    while y>=0:
        plot_points(xes,yes,x,y,xc,yc)
        if p2>0:
            y-=1
            p2-=2*rx*rx*y+rx*rx
        else:
            x+=1
            y-=1
            p2+=2*ry*ry*x-2*rx*rx*y+rx*rx
        plot_points(xes,yes,x,y,xc,yc)
    plt.grid()
    plt.scatter(xes, yes)
    plt.show()                                  
def plot_points(xes,yes,x,y,xc,yc):
    xes.append(x+xc)
    yes.append(y+yc)
    xes.append(-x+xc)
    yes.append(y+yc) 
    xes.append(-x+xc)
    yes.append(-y+yc) 
    xes.append(x+xc)
    yes.append(-y+yc) 
xc=int(input("enter the value of xc"))
yc=int(input("enter the value of yc"))
rx=int(input("enter the value of rx"))
ry=int(input("enter the value of ry"))
midpoint_ellipse(rx,ry,xc,yc)
