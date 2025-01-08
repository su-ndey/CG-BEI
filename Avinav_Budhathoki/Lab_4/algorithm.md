# Algorithm for Midpoint Ellipse Drawing Algorithm

## Input:
- `rx`: Radius along the x-axis
- `ry`: Radius along the y-axis
- `xc`, `yc`: Coordinates of the center of the ellipse

## Output:
- A plotted ellipse using the midpoint algorithm

## Steps:

### Step 1: Initialize variables
1. Start with \( x = 0 \) and \( y = ry \).
2. Compute initial decision parameters:
   - \( ry^2 \) and \( rx^2 \)
   - \( p1 = ry^2 - (rx^2 \times ry) + (0.25 \times rx^2) \)

### Step 2: Region 1 processing
- Repeat while \( 2 \times ry^2 \times x \leq 2 \times rx^2 \times y \):
  1. Plot the points for the current \( x \) and \( y \) values using symmetrical properties.
  2. Update \( x \) by incrementing it by 1.
  3. Update decision parameter:
     - If \( p1 < 0 \):
       - \( p1 = p1 + 2 \times ry^2 \times x + ry^2 \)
     - Else:
       - \( y = y - 1 \)
       - \( p1 = p1 + 2 \times ry^2 \times x - 2 \times rx^2 \times y + ry^2 \)

### Step 3: Region 2 processing
1. Compute the initial decision parameter for Region 2:
   - \( p2 = (ry^2 \times (x + 0.5)^2) + (rx^2 \times (y - 1)^2) - (rx^2 \times ry^2) \)
2. Repeat while \( y \geq 0 \):
   1. Plot the points for the current \( x \) and \( y \) values using symmetrical properties.
   2. Update \( y \) by decrementing it by 1.
   3. Update decision parameter:
      - If \( p2 > 0 \):
        - \( p2 = p2 - 2 \times rx^2 \times y + rx^2 \)
      - Else:
        - \( x = x + 1 \)
        - \( p2 = p2 + 2 \times ry^2 \times x - 2 \times rx^2 \times y + rx^2 \)

### Step 4: Plot the points
- Use a helper function to plot all four symmetrical points for each calculated \( x \) and \( y \):
  - \( (x + xc, y + yc) \)
  - \( (-x + xc, y + yc) \)
  - \( (-x + xc, -y + yc) \)
  - \( (x + xc, -y + yc) \)

### Step 5: Display the ellipse
- Use `matplotlib.pyplot.scatter` to visualize the computed points.

---
