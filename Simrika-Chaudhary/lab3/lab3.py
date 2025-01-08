import matplotlib.pyplot as plt
def plot_point(xes,yes,x,y,xc,yc):
    xes.append(x+xc) 
    yes.append(y+yc)
       
    xes.append(-x+xc) 
    yes.append(y+yc)
       
    xes.append(-x+xc) 
    yes.append(-y+yc)
       
    xes.append(x+xc) 
    yes.append(-y+yc)
       
    xes.append(y+yc) 
    yes.append(x+xc)
       
    xes.append(-y+yc) 
    yes.append(x+xc)
       
    xes.append(y+yc) 
    yes.append(-x+xc)
       
    xes.append(-y+yc) 
    yes.append(-x+xc)
       
def midpoint_circle(r,xc,yc):
   x=0
   y=r
   p=1-r
   xes=[]
   yes=[]
   plot_point(xes,yes,x,y,xc,yc)
   while x<y:
        x=x+1
        if(p<0):
            p=p+2*x+1
        else: 
            y=y-1
            p=p+2*(x-y)+1
        plot_point(xes,yes,x,y,xc,yc)
    
    
   return xes,yes

r=(int(input("enter the radius of the circle:")))
xc=(int(input("enter the x-cordinates for the centre of circle:")))
yc=(int(input("enter the y-cordinates for the centre of circle:")))
a,b=midpoint_circle(r,xc,yc)
plt.scatter(a,b)
plt.show()
    
          
   
   
   
   