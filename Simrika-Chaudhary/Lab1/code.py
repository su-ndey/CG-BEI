import matplotlib.pyplot as plt 
def dda(x0,y0,x1,y1):
    del_x=x1-x0;
    del_y=y1-y0;
    steps=max(abs(del_x),abs(del_y))
    x_inc=del_x/steps
    y_inc=del_y/steps
    x=x0
    y=y0
    xes=[]
    yes=[]
    for i in range(steps):
        xes.append(x)
        yes.append(y)
        x=x+x_inc
        y=y+y_inc
    print(xes)
    print(yes)
    plt.plot(xes,yes,marker='*')
    plt.show()
x0=int(input('Enter the value of x0'))
y0=int(input('Enter the value of y0'))
x1=int(input('Enter the value of x1'))
y1=int(input('Enter the value of y1'))
dda(x0,y0,x1,y1)

