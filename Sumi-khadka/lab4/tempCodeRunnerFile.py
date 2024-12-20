plot_points(xes,yes,x,xc,y,yc)
        if p2>0:
            y-=1
            p2-=2*rx**2*y+rx**2
        else:
            x+=1
            y-=1
            p2+=2*ry**2*x-2*rx**2*y+rx**2
        plot_points(xes,yes,x,y,xc,yc)