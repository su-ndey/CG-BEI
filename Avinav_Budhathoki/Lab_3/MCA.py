import matplotlib.pyplot as plt

def plotCircle(xes,yes,x,y,xc,yc): 
    xes.extend([x+xc,-x+xc,-x+xc,x+xc,y+xc,-y+xc,y+xc,-y+xc])
    yes.extend([y+yc,y+yc,-y+yc,-y+yc,x+yc,x+yc,-x+yc,-x+yc])
    

def drawCircle():
    r  = int(input("enter the radius:"))
    xc = int(input("enter the x-cordinate of the center of the circle: "))
    yc = int(input("enter the y-cordinate of the center of the circle: "))
   
    x = 0
    y = r 
    p = 1-r 
    
    xes = []
    yes = []
    
    plotCircle(xes, yes, x, y, xc, yc)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2*x + 1
        else:
            y -= 1
            p = p + 2*(x-y) + 1 
        
        plotCircle(xes, yes, x, y, xc, yc)
    
    plt.title("Midpoint Circle Drawing Algorithm")
    plt.scatter(xes,yes,marker='o')
    plt.grid(True)
    plt.savefig("output.png")

drawCircle()