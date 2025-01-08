# Midpoint Circle Algorithm

This repository contains a Python implementation of the **Midpoint Circle Algorithm**, a classic algorithm for drawing circles using symmetry and integer calculations. It is widely used in computer graphics for rasterizing circles efficiently.

## Algorithm Overview

The Midpoint Circle Algorithm is an iterative process that determines the points needed to draw a circle, leveraging the circle's symmetry to reduce computation. The key idea is to use a decision parameter to choose the next pixel to plot, minimizing floating-point operations.

## Algorithm Steps

1. **Input:**
   - Radius of the circle (`r`).
   - Coordinates of the circle center (`xc`, `yc`).

2. **Initialization:**
   - Set initial values: `x = 0`, `y = r`.
   - Compute the initial decision parameter: `p = 1 - r`.

3. **Plot Initial Point:**
   - Plot the initial point and its symmetric counterparts in all octants.

4. **Iterate While `x < y`:**
   - Increment `x` by 1.
   - Update the decision parameter:
     - If `p < 0`, keep `y` unchanged and update `p = p + 2x + 1`.
     - Otherwise, decrement `y` by 1 and update `p = p + 2(x - y) + 1`.
   - Plot the current point and its symmetric counterparts.

5. **Visualization:**
   - Use a plotting library like `matplotlib` to visualize the calculated points.
