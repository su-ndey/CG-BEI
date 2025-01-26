import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Function to draw a line
def draw_line():
    glLineWidth(10)  # Set line width
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glVertex2f(-0.5, 0.0)  # Start point of the line
    glVertex2f(0.5, 0.0)   # End point of the line
    glEnd()

# Function to draw a red rectangle
def draw_red_rectangle():
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glVertex2f(-0.7, -0.5)  # Bottom left
    glVertex2f(-0.7, -0.2)  # Top left
    glVertex2f(-0.3, -0.2)  # Top right
    glVertex2f(-0.3, -0.5)  # Bottom right
    glEnd()

# Function to draw a blue rectangle
def draw_blue_rectangle():
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glVertex2f(0.3, -0.5)   # Bottom left
    glVertex2f(0.3, -0.2)   # Top left
    glVertex2f(0.7, -0.2)   # Top right
    glVertex2f(0.7, -0.5)   # Bottom right
    glEnd()

# Function to draw a cyan polygon
def draw_cyan_polygon():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Cyan color
    glVertex2f(0.0, 0.5)  # Top point
    glVertex2f(-0.3, 0.2)  # Bottom left
    glVertex2f(0.3, 0.2)  # Bottom right
    glEnd()

# Set up OpenGL environment (background color, depth testing, etc.)
def setup():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    glEnable(GL_DEPTH_TEST)  # Enable depth testing (for 3D rendering)
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)  # Orthographic projection (2D)

# The function to handle drawing
def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear screen and depth buffer
    
    draw_line()             # Draw the red line
    draw_red_rectangle()    # Draw the red rectangle
    draw_blue_rectangle()   # Draw the blue rectangle
    draw_cyan_polygon()     # Draw the cyan polygon

    glfw.swap_buffers(window)  # Swap buffers to display the drawn content

# Main function to create window, process user input, and render primitives
def main():
    if not glfw.init():
        return

    global window
    window = glfw.create_window(800, 600, "2D Shapes", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    setup()  # Set up OpenGL environment

    while not glfw.window_should_close(window):
        draw()  # Draw the shapes
        glfw.poll_events()  # Poll for events

    glfw.terminate()  # Terminate GLFW

if __name__ == "__main__":
    main()
