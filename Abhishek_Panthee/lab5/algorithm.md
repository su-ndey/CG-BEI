### Algorithm: Line Drawing and Transformation

1. **Input:**
   - Take starting point \((x_1, y_1)\) and ending point \((x_2, y_2)\).
   - Input rotation angle (\(angle\)) in degrees.
   - Input scaling factors \(sx\) and \(sy\).

2. **Draw Line (Bresenham's Algorithm):**
   - Calculate:
     - \(dx = |x_2 - x_1|\)
     - \(dy = |y_2 - y_1|\)
   - Determine step directions:
     - \(sx = 1\) if \(x_2 > x_1\), else \(-1\).
     - \(sy = 1\) if \(y_2 > y_1\), else \(-1\).
   - Initialize decision parameter \(p\):
     - If \(dx \geq dy\), \(p = 2dy - dx\).
     - Else, \(p = 2dx - dy\).
   - Loop through and calculate points:
     - Add current \((x, y)\) to the list.
     - Update \(p\) and adjust \(x\) or \(y\) based on the condition.

3. **Apply Scaling:**
   - Multiply each \(x\)-coordinate by \(sx\).
   - Multiply each \(y\)-coordinate by \(sy\).

4. **Apply Rotation:**
   - Convert \(angle\) to radians: \(\text{angle (radians)} = \text{angle (degrees)} \times \pi / 180\).
   - For each point \((x, y)\), calculate:
     - \(x' = x \cdot \cos(\text{angle}) - y \cdot \sin(\text{angle})\).
     - \(y' = x \cdot \sin(\text{angle}) + y \cdot \cos(\text{angle})\).

5. **Output:**
   - Plot the original line.
   - Plot the scaled line.
   - Plot the rotated line.

6. **End.**

