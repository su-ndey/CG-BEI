1. Input:
   - Radii `r_x`, `r_y`.
   - Center coordinates `x_c`, `y_c`.

2. Initialization:
   - Set `x = 0`, `y = r_y`.
   - Calculate the initial decision parameter for Region 1:
     P1 = r_y^2 - (r_x^2 * r_y) + (0.25 * r_x^2)

3. Region 1 (Slope > -1):
   - While (2 * r_y^2 * x < 2 * r_x^2 * y):
     a. Plot points:
        (x + x_c, y + y_c), (x + x_c, -y + y_c),
        (-x + x_c, y + y_c), (-x + x_c, -y + y_c)
     b. If (P1 < 0):
        - Increment x: x = x + 1
        - Update P1: P1 = P1 + 2 * r_y^2 * x + r_y^2
     c. Else:
        - Increment x: x = x + 1
        - Decrement y: y = y - 1
        - Update P1: P1 = P1 + 2 * r_y^2 * x - 2 * r_x^2 * y + r_y^2

4. Region 2 (Slope ≤ -1):
   - Calculate the initial decision parameter:
     P2 = r_y^2 * (x + 0.5)^2 + r_x^2 * (y - 1)^2 - r_x^2 * r_y^2
   - While (y >= 0):
     a. Plot points:
        (x + x_c, y + y_c), (x + x_c, -y + y_c),
        (-x + x_c, y + y_c), (-x + x_c, -y + y_c)
     b. If (P2 > 0):
        - Decrement y: y = y - 1
        - Update P2: P2 = P2 - 2 * r_x^2 * y + r_x^2
     c. Else:
        - Increment x: x = x + 1
        - Decrement y: y = y - 1
        - Update P2: P2 = P2 + 2 * r_y^2 * x - 2 * r_x^2 * y + r_x^2

5. End:
   - The ellipse is drawn.
