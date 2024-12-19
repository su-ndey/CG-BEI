import matplotlib.pyplot as plt
def plot(xes,yes,x,y,xc,yc): 
    
    xes.extend([x+xc,-x+xc,-x+xc,x+xc,y+xc,-y+xc,y+xc,-y+xc])
    yes.extend([y+yc,y+yc,-y+yc,-y+yc,x+yc,x+yc,-x+yc,-x+yc])
    


def MCA():

    r  = int(input("enter the radius value :"))
    xc = int(input("enter the value of x centre:"))       
    yc = int(input("enter the value of y centre:"))
   
    x=0
    y=r
    p = 1-r # Initialization
    
    xes = [] #x co ordinate list
    yes = [] #y co ordinate list
    
    plot(xes,yes,x,y,xc,yc)
    
    while x < y:
        x = x+1 
        if p < 0:
            p = p + 2*x + 1

        else:
            y = y - 1
            p = p + 2*(x-y) + 1 

        plot(xes,yes,x,y,xc,yc)     # calling plot function
    
    plt.scatter(xes,yes,marker='o')   # Plotting each point
    plt.grid(True)
    plt.show()

MCA()   
 
    