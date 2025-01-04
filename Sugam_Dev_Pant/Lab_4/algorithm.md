# Midpoint Ellipse Drawing Algorithm

## Steps of the Algorithm

### Initialization
1. Define the radii of the ellipse as `rx` and `ry`.
2. Set the center coordinates of the ellipse as `xc` and `yc`.
3. Initialize the starting point at:
   - x = 0
   - y = ry
4. Compute the squared values for radii:
   - rx²
   - ry²
5. Compute the initial decision parameter for Region 1:
   - p1 = ry² - (rx² * ry) + (0.25 * rx²)
6. Calculate initial increments:
   - dx = 2 * ry² * x
   - dy = 2 * rx² * y

### Region 1: Decision Parameter Iteration
1. While dx < dy:
   - Plot points for all four quadrants:
     - (x + xc, y + yc)
     - (-x + xc, y + yc)
     - (x + xc, -y + yc)
     - (-x + xc, -y + yc)
   - If p1 < 0:
     - Increment x by 1.
     - Update dx += 2 * ry².
     - Update p1 += dx + ry².
   - Else:
     - Increment x by 1 and decrement y by 1.
     - Update dx += 2 * ry².
     - Update dy -= 2 * rx².
     - Update p1 += dx - dy + ry².

### Region 2: Decision Parameter Iteration
1. Compute the initial decision parameter for Region 2:
   - p2 = (ry² * (x + 0.5)²) + (rx² * (y - 1)²) - (rx² * ry²)
2. While y >= 0:
   - Plot points for all four quadrants:
     - (x + xc, y + yc)
     - (-x + xc, y + yc)
     - (x + xc, -y + yc)
     - (-x + xc, -y + yc)
   - If p2 > 0:
     - Decrement y by 1.
     - Update dy -= 2 * rx².
     - Update p2 += rx² - dy.
   - Else:
     - Increment x by 1 and decrement y by 1.
     - Update dx += 2 * ry².
     - Update dy -= 2 * rx².
     - Update p2 += dx - dy + rx².

### Final Visualization
- Plot all the calculated points for the ellipse.
- Ensure proper scaling for axes to maintain the elliptical shape.
