# Bresenham's Line Drawing Algorithm (BA)

## Algorithm Steps

### Input
- **x1, y1**: Coordinates of the starting point
- **x2, y2**: Coordinates of the ending point

### Output
- A list of x and y coordinates representing points along the line.

---

### Steps

1. **Calculate the Absolute Differences**  
   - Compute the differences in x and y coordinates:  
     `dx = |x2 - x1|`  
     `dy = |y2 - y1|`

2. **Initialize Direction Variables**  
   - Determine the x-direction (`sx`):  
     - `IF x2 > x1 THEN sx = 1 ELSE sx = -1`  
   - Determine the y-direction (`sy`):  
     - `IF y2 > y1 THEN sy = 1 ELSE sy = -1`

3. **Initialize Coordinates**  
   - Start with:  
     `x = x1`  
     `y = y1`  
   - Create empty lists to store coordinates:  
     `xes = []`  
     `yes = []`

4. **Choose Line Drawing Method**  
   - Check the slope of the line:  
     **IF dx >= dy** (more horizontal line):  
     - a) Initialize the decision parameter:  
        `Po = (2 * dy) - dx`  
        `Pk = Po`  
     - b) Iterate while `x < x2`:  
        - Append current `(x, y)` to `xes` and `yes`.  
        - Increment `x` by `sx`.  
        - Update `Pk`:  
          - `IF Pk >= 0`:  
            Increment `y` by `sy` and set `Pk = Pk + 2 * dy - 2 * dx`.  
          - `ELSE`:  
            Set `Pk = Pk + 2 * dy`.  

     **ELSE** (more vertical line):  
     - a) Initialize the decision parameter:  
        `Po = (2 * dx) - dy`  
        `Pk = Po`  
     - b) Iterate while `y < y2`:  
        - Append current `(x, y)` to `xes` and `yes`.  
        - Increment `y` by `sy`.  
        - Update `Pk`:  
          - `IF Pk >= 0`:  
            Increment `x` by `sx` and set `Pk = Pk + 2 * dx - 2 * dy`.  
          - `ELSE`:  
            Set `Pk = Pk + 2 * dx`.

5. **Visualization**  
   - Plot points in `xes` and `yes` using **matplotlib**.  
   - Display the plot with markers.

---

### Termination Condition
- The line drawing stops when `x` reaches `x2`.