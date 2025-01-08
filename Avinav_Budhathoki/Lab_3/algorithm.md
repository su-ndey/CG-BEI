# Midpoint Circle Drawing Algorithm

## Purpose:
This algorithm is used to draw a circle on a 2D plane given a radius and the coordinates of the center using the Midpoint Circle Drawing method.

## Steps:

### 1. Input Parameters:
- The user is prompted to input the following values:
  - **radius (r)**: The radius of the circle.
  - **xc**: The x-coordinate of the center of the circle.
  - **yc**: The y-coordinate of the center of the circle.

### 2. Initialization:
- Set initial values for:
  - **x = 0**
  - **y = r** (initial y-coordinate at the top of the circle)
  - **p = 1 - r** (initial value of the decision parameter)

### 3. Generate Circle Points:
- Use the Midpoint Circle Drawing Algorithm to calculate the points on the circle:
  - Plot the initial points (x, y) along with their symmetric counterparts in all octants.
  - Use the following rules to calculate new points:
    - If the decision parameter **p** is less than 0, move to the next point in the same x-direction (i.e., increase x).
    - If the decision parameter **p** is greater than or equal to 0, move diagonally (i.e., decrease y and increase x).
  
  These points are stored in **xes** (x-coordinates) and **yes** (y-coordinates) arrays.

### 4. Plotting:
- After the loop completes, plot all the points stored in **xes** and **yes**.
- The points are plotted using `plt.scatter()`, and the plot is titled "Midpoint Circle Drawing Algorithm".
- The grid is enabled for better visualization.
  
### 5. Output:
- The resulting circle is saved as a PNG image file named **output.png**.

## Code Walkthrough:

1. **plotCircle()** function: 
   - This function calculates and appends the symmetric points of the circle based on the center (xc, yc) and the current point (x, y). These points are added to the lists **xes** and **yes**.

2. **drawCircle()** function:
   - Takes user input for the radius and center coordinates.
   - Initializes values for **x**, **y**, and **p**.
   - Uses a while loop to calculate the points of the circle by checking the value of the decision parameter **p** and updating **x** and **y** accordingly.
   - The `plotCircle()` function is called at each step to add the new points.
   - Finally, it generates and saves the circle plot.