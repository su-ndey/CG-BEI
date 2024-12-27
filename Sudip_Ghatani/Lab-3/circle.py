import matplotlib.pyplot as plt
def plot(xes,yes,x,y,xc,yc):
    
    xes.extend([x+xc,-x+xc,-x+xc,x+xc,y+xc,-y+xc,y+xc,-y+xc])
    yes.extend([y+yc,y+yc,-y+yc,-y+yc,x+yc,x+yc,-x+yc,-x+yc])
    

def mid_circle():
    print("1.Circle with center at origin origin\n2.Circule with centre (x,y)\n")
    choice = int(input())
    xc = 0
    yc = 0
    r = 0
    if choice == 1:
        r  = int(input("enter the radius:"))
    if choice == 2:
        r  = int(input("enter the radius:"))
        xc = int(input("enter the centre x:"))   
        yc = int(input("enter the centre y:"))
        
   
    x = 0
    y = r
    p = 1 - r
    
    
    xes = []
    yes = []
    
    plot(xes,yes,x,y,xc,yc)
    
        

    while x < y:
        x = x+1 
        if p < 0:
            p = p + 2*x + 1

        else:
            y = y - 1
            p = p + 2*(x-y) + 1 

        plot(xes,yes,x,y,xc,yc)
    
    plt.scatter(xes,yes,marker='o')
    plt.grid(True)
    plt.show()

mid_circle()   