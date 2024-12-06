# Bresenham's Line Drawing Algorithm

This program implements Bresenham's Line Drawing Algorithm to draw a line between two points in a 2D plane.

## Steps:
1. **Input:**
   - Prompt the user to input the starting point \((x_1, y_1)\) and the ending point \((x_2, y_2)\).

2. **Initialize Variables:**
   - Compute the differences:
     - \( dx = |x_2 - x_1| \)
     - \( dy = |y_2 - y_1| \)
   - Determine step directions:
     - \( sx = 1 \) if \( x_2 > x_1 \), otherwise \( sx = -1 \).
     - \( sy = 1 \) if \( y_2 > y_1 \), otherwise \( sy = -1 \).
   - Set starting point:
     - \( x = x_1 \), \( y = y_1 \).
   - Prepare empty lists to store coordinates (`xes` and `yes`).

3. **Determine Line Type:**
   - **Case 1: Line is more horizontal (\(dx \geq dy\)):**
     - Compute the decision parameter:
       - \( p = 2 \cdot dy - dx \)
     - For \( dx + 1 \) iterations:
       - Append the current \( x, y \) to the coordinate lists.
       - Update \( y \) and \( p \) based on the decision parameter.
       - Increment \( x \) by \( sx \).
   - **Case 2: Line is more vertical (\(dx < dy\)):**
     - Compute the decision parameter:
       - \( p = 2 \cdot dx - dy \)
     - For \( dy + 1 \) iterations:
       - Append the current \( x, y \) to the coordinate lists.
       - Update \( x \) and \( p \) based on the decision parameter.
       - Increment \( y \) by \( sy \).

4. **Plot the Line:**
   - Use `matplotlib` to plot the computed points as a line.
   - Enable grid on the plot.
   - Save the output as `plot_output.png`.

5. **Output:**
   - The program saves the plotted image as `plot_output.png` in the working directory.
   - Print a confirmation message to the user.

## How to Run:
1. Ensure Python 3 and `matplotlib` are installed on your system.
2. Run the script using:
   ```bash
   python3 code.py

    