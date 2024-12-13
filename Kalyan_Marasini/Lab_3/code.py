import matplotlib.pyplot as plt

def plot_points(xes, yes, x, y, xc, yc):
    xes.extend([x + xc, -x + xc, -x + xc, x + xc, y + xc, -y + xc, y + xc, -y + xc])
    yes.extend([y + yc, y + yc, -y + yc, -y + yc, x + yc, x + yc, -x + yc, -x + yc])

def draw_circle():
    r = int(input("Enter the radius of the circle:"))
    xc = int(input("Enter the value of x-coordinate where the circle is centered at:"))       
    yc = int(input("Enter the value of y-ccordinate where the circle is centered at:"))
   
    x = 0
    y = r
    p = 1 - r
    
    xes = []
    yes = []
    
    plot_points(xes, yes, x, y, xc, yc)

    while x < y:
        x += 1 
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1 

        plot_points(xes, yes, x, y, xc, yc)
    
    plt.scatter(xes, yes, marker='o')
    plt.grid(True)
    plt.show()

draw_circle()

