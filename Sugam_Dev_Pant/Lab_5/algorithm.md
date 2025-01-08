# Bresenham's Line Drawing Algorithm and 2D Transformations

## Overview

This document describes the algorithms for:
1. **Bresenham's Line Drawing Algorithm**
2. **Scaling Transformation**
3. **Fixed-Point Rotation Transformation**

Each algorithm includes an explanation of the logic behind it and how it is implemented in the context of plotting lines and applying transformations.

## 1. Bresenham's Line Drawing Algorithm

Bresenham's algorithm is an efficient method for drawing a straight line between two points on a grid. It decides which points to plot based on the decision variable and avoids using floating-point arithmetic, which is faster and more efficient.

### Steps:
1. **Input:** Two endpoints of the line, `(x0, y0)` and `(x1, y1)`.
2. **Calculate Differences:**
   - `dx = |x1 - x0|`
   - `dy = |y1 - y0|`
   - Determine the step direction for `x` and `y` using `sx = (1 if x1 > x0 else -1)` and `sy = (1 if y1 > y0 else -1)`.
3. **Decision Variable:**
   - For lines with a steep slope (`dx >= dy`), calculate `p = 2 * dy - dx` and start plotting from `(x0, y0)`.
   - For lines with a shallow slope (`dy > dx`), calculate `p = 2 * dx - dy` and start plotting similarly.
4. **Iterate:**
   - Update `x` or `y` depending on the value of the decision variable `p`.
   - If `p >= 0`, increment the other coordinate and adjust `p` accordingly.
   - Continue this process until the end point `(x1, y1)` is reached.

### Output:
- The set of points `(x, y)` that form the line between the two endpoints.

---

## 2. Scaling Transformation

Scaling is a geometric transformation that enlarges or reduces an object by multiplying its coordinates by scale factors along the x and y axes. The scaling can be uniform or non-uniform, depending on the scale factors provided.

### Steps:
1. **Input:** 
   - Coordinates of the points forming the object (e.g., a line).
   - Scaling factors `scale_x` (for the x-axis) and `scale_y` (for the y-axis).
2. **Transform Coordinates:**
   - For each point `(x, y)`, apply the scaling transformation:
     - `x_scaled = x * scale_x`
     - `y_scaled = y * scale_y`
3. **Output:** 
   - The transformed points `(x_scaled, y_scaled)` form the scaled object.

---

## 3. Fixed-Point Rotation Transformation

Rotation is a geometric transformation that turns an object around a fixed point by a specified angle. Fixed-point rotation means the object rotates around a specific point (typically one of the object's original points).

### Steps:
1. **Input:** 
   - Coordinates of the points forming the object (e.g., a line).
   - The rotation angle `theta` in degrees.
   - The fixed point `(fx, fy)` around which the object will be rotated (often one of the endpoints of the line).
2. **Translate the Fixed Point to the Origin:**
   - Apply a translation transformation to move the fixed point `(fx, fy)` to the origin `(0, 0)`. This is achieved by subtracting `fx` and `fy` from the coordinates.
   - Translation matrix:
     ``` 
     translation_to_origin = [
         [1, 0, -fx],
         [0, 1, -fy],
         [0, 0, 1]
     ]
     ```
3. **Apply Rotation:**
   - Use the 2D rotation matrix to rotate the points:
     ``` 
     rotation_matrix = [
         [cos(theta), -sin(theta), 0],
         [sin(theta), cos(theta), 0],
         [0, 0, 1]
     ]
     ```
4. **Translate Back to the Original Position:**
   - Apply the inverse translation transformation to move the object back to its original position.
   - Inverse translation matrix:
     ``` 
     inverse_translation = [
         [1, 0, fx],
         [0, 1, fy],
         [0, 0, 1]
     ]
     ```
5. **Composite Transformation:**
   - Combine the translation, rotation, and inverse translation transformations into one composite matrix:
     ```
     composite_matrix = inverse_translation @ rotation_matrix @ translation_to_origin
     ```
6. **Apply the Transformation:**
   - Multiply the original coordinates by the composite transformation matrix to get the rotated points.

### Output:
- The transformed points `(x_rotated, y_rotated)` form the rotated object.

---

## Conclusion

This document outlines the algorithms used for Bresenham's line drawing, scaling, and rotation transformations in a 2D plane. By understanding the underlying principles of these algorithms, you can efficiently manipulate and transform geometric objects in applications such as computer graphics, robotics, and game development.
