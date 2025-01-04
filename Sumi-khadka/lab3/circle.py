import matplotlib.pyplot as plt
def plot_points(xes,yes,x,y):
    xes.append(x)
    yes.append(y)
    xes.append(-x)
    yes.append(y) 
    xes.append(-x)
    yes.append(-y) 
    xes.append(x)
    yes.append(-y) 
    xes.append(y)
    yes.append(x) 
    xes.append(-y)
    yes.append(x) 
    xes.append(y)
    yes.append(-x) 
    xes.append(-y)
    yes.append(-x)

def mid_point_circle(r):
    x = 0
    y = r
    p=1-r
    xes=[]
    yes=[]
    plot_points(xes,yes,x,y)
    while(x<y):
        x=x+1
        if p<0:
             p=p+2*x+1
        else:
            y=y-1
            p=p+2*(x-y)+1
        plot_points(xes,yes,x,y)

    plt.grid()
    plt.scatter(xes, yes)
    plt.show()

rad= int(input("enter r:"))
mid_point_circle(rad)