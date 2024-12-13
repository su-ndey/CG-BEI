import matplotlib.pyplot as plt

def circle(r):
    x=int(0)
    y=int(r)
    p=(1-r)
    xes = []
    yes = []
    while(x<y):
        xes.extend([x,x,y,-y,-x,-x,-y,y])
        yes.extend([y,-y,-x,-x,-y,y,x,x])
        x= x + 1
        if p<0 :
            p = p + 2*x + 1
        if p>=0 :
            y = y - 1
            p = p + 2*(x-y) + 1
    plt.grid()
    plt.scatter(xes, yes, marker='o')
    plt.show()
r=int(input("enter radius"))
circle(r)