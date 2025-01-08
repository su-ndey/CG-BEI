# DDA Line Drawing Algorithm

This Python program implements the **DDA (Digital Differential Analyzer) Line Drawing Algorithm** to generate a straight line between two points in a 2D plane. The resulting line is plotted and saved as an image.

---

## **Algorithm Steps**

### **Input:**
- Coordinates of the starting point \((x_0, y_0)\).
- Coordinates of the ending point \((x_1, y_1)\).

### **Output:**
- A list of calculated points for the line.
- A plotted image saved as `dda-op-image.png`.

---

### **Steps:**

1. **Initialize Variables:**
   - Compute differences in the coordinates:
     - \( \Delta x = x_1 - x_0 \)
     - \( \Delta y = y_1 - y_0 \)
   - Determine the number of steps required:
     - \( \text{steps} = \max(|\Delta x|, |\Delta y|) \)
   - Calculate the increments for each step:
     - \( x_{\text{increment}} = \frac{\Delta x}{\text{steps}} \)
     - \( y_{\text{increment}} = \frac{\Delta y}{\text{steps}} \)

2. **Generate Line Points:**
   - Initialize \( x = x_0 \), \( y = y_0 \).
   - Create empty lists `xes` and `yes` to store \( x \) and \( y \) coordinates.
   - For \( \text{steps} + 1 \) iterations:
     - Append the rounded \( x \) and \( y \) values to `xes` and `yes`.
     - Update \( x \) and \( y \):
       - \( x = x + x_{\text{increment}} \)
       - \( y = y + y_{\text{increment}} \)

3. **Plot the Line:**
   - Use `matplotlib` to plot the points stored in `xes` and `yes`.
   - Add axis labels, grid, and a title to the plot.
   - Save the plotted image as `dda-op-image.png`.

4. **Display Output:**
   - Print or save the generated points and plot.

---

## **How to Run:**

1. **Ensure Requirements:**
   - Install Python 3 and `matplotlib` on your system.

2. **Run the Program:**
   - Execute the script:
     ```bash
     python3 dda_line.py
     ```
   - Enter the starting and ending coordinates when prompted:
     ```bash
     Enter the values of x0, y0, x1, y1: 2 3 10 8
     ```

3. **Output:**
   - The generated line points will be plotted and saved as `dda-op-image.png`.

---

## **Example Input and Output**

### **Input:**
