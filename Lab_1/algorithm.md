# Digital Differential Analyzer (DDA) Line Drawing Algorithm

## Algorithm Steps

1. **Input the Starting and Ending Coordinates**
   - Get the coordinates of the starting point (x0, y0) and the ending point (x1, y1).

2. **Calculate the Differences**
   - Calculate the differences in the x and y directions:
     - sugX = x1 - x0
     - ΔY = y1 - y0

3. **Determine the Number of Steps**
   - The number of steps required is the maximum of the absolute differences:
     - steps = max(|ΔX|, |ΔY|)

4. **Calculate the Increment for Each Step**
   - Calculate the increments for x and y:
     - xIncrement = ΔX / steps
     - yIncrement = ΔY / steps

5. **Initialize the Starting Point**
   - Start at (x0, y0).

6. **Iterate Through the Number of Steps**
   - For each step from 0 to `steps`:
     - Plot the current point (x, y).
     - Increment x and y:
       - x = x + xIncrement
       - y = y + yIncrement

7. **Stop Once All Steps Are Plotted**
   - End the iteration after plotting all points, resulting in a line from (x0, y0) to (x1, y1).
