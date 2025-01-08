import matplotlib.pyplot as plt

def midpoint_ellipse(rx,ry,xc,yc):
    x=0
    y=ry
    ry2=ry*ry
    rx2=rx*rx
    p1=ry2-(rx2*ry)+(0.25*rx2)
    xes=[]
    yes=[]
    while 2*ry2*x<=2*rx2*y:
        plot(xes,yes,x,y,xc,yc)
        

        if p1<0:
            x+=1
            p1+=2*ry2*x+ry2
        else:
            x+=1
            y-=1
            p1+=2*ry2*x-2*rx2*y+ry2
        
    p2=(ry2*(x+0.5)**2)+(rx2*(y-1)**2)-(rx2*ry2)

    while y>=0:
       

        if p2>0:
            y-=1
            p2-=2*rx2*y+rx2
        else:
            x+=1
            y-=1
            p2+=2*ry2*x-2*rx2*y+rx2
        plot(xes,yes,x,y,xc,yc)
    plt.scatter(xes,yes)
    plt.show()

def plot(xes,yes,x,y,xc,yc):
    xes.append(x+xc)
    yes.append(y+yc)

    xes.append(-x+xc)
    yes.append(y+yc)

    xes.append(-x+xc)
    yes.append(-y+yc)

    xes.append(x+xc)
    yes.append(-y+yc)


xc = int(input("Enter the x-coord for ellipse: "))
yc = int(input("Enter the y-coord for ellipse: "))
rx = int(input("Enter the rx value: "))
ry = int(input("Enter the ry value: "))
midpoint_ellipse(rx,ry,xc,yc)