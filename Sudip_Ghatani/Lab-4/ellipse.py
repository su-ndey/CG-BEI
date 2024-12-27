import matplotlib.pyplot as plt

rx = int(input("Enter first radius: "))
ry = int(input("Enter second radius: "))
xc = int(input("Enter x-axis radius: "))
yc = int(input("Enter y-axis radius: "))

def midpoint_ellipse(rx,ry,xc,yc):
    x = 0
    y = ry
    xes = []
    yes = []
    
    p1 = (ry**2) - (rx**2 * ry) + ((1/4) * rx**2)
    
    
    while (2*ry**2*x) <= (2*rx**2*y):
        xes = [x+xc,-x+xc,x+xc,-x+xc]
        yes = [y+yc,y+yc,-y +yc,-y +yc]
        plt.scatter(xes,yes)
        print("end1")
    
        if p1 < 0:
            x += 1
        
            p1 = 2*ry**2*x + ry**2
        else:
            y-= 1 
            x += 1
            p1 = 2*ry**2 *x - 2*rx**2 * y + ry**2
        
    p2 = (ry**2*(x+0.5)**2)+(rx**2*(y-1)**2)-(rx**2 * ry**2)
    
    while y>=0:
        xes = [x+xc,-x+xc,x+xc,-x+xc,]
        yes = [y+yc,y+yc,-y +yc,-y +yc]
        plt.scatter(xes,yes)
        print("end2")
      
        if p2 > 0:
            y-=1
            p2 -= 2*rx**2*y + rx**2
        else:
            x+=1
            y-=1
            p2+= 2*ry^2*x - 2*rx**2*y + rx**2
        
       
midpoint_ellipse(rx,ry,xc,yc)
plt.grid(True)
plt.show()

