# Digital Differential Analyzer (DDA) Line Drawing Algorithm

## Algorithm Steps

### 1. Input the Starting and Ending Coordinates
   - Get the coordinates of the starting point \((x_0, y_0)\) and the ending point \((x_1, y_1)\).

### 2. Calculate the Differences
   - Calculate the differences in the x and y directions:
     \[
     \Delta X = x_1 - x_0, \quad \Delta Y = y_1 - y_0
     \]

### 3. Determine the Number of Steps
   - The number of steps required is the maximum of the absolute differences:
     \[
     \text{steps} = \max(|\Delta X|, |\Delta Y|)
     \]

### 4. Calculate the Increment for Each Step
   - Calculate the increments for x and y:
     \[
     x_{\text{Increment}} = \frac{\Delta X}{\text{steps}}, \quad y_{\text{Increment}} = \frac{\Delta Y}{\text{steps}}
     \]

### 5. Initialize the Starting Point
   - Start at \((x_0, y_0)\).

### 6. Iterate Through the Number of Steps
   - For each step from 0 to `steps`:
     - Plot the current point \((x, y)\).
     - Increment \(x\) and \(y\):
       \[
       x = x + x_{\text{Increment}}, \quad y = y + y_{\text{Increment}}
       \]

### 7. Stop Once All Steps Are Plotted
   - End the iteration after plotting all points, resulting in a line from \((x_0, y_0)\) to \((x_1, y_1)\).
