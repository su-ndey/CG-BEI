import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Function to draw various primitives
def draw_primitives():
    # Draw a line
    glLineWidth(10)  # Set line width
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)  # White color for the line
    glVertex2f(-0.5, 0.5)  # Start point
    glVertex2f(0.5, 0.5)  # End point
    glEnd()

    # Draw a red rectangle
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glVertex2f(-0.8, -0.2)  # Bottom-left
    glVertex2f(-0.2, -0.2)  # Bottom-right
    glVertex2f(-0.2, -0.8)  # Top-right
    glVertex2f(-0.8, -0.8)  # Top-left
    glEnd()

    # Draw a blue rectangle
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glVertex2f(0.2, -0.2)  # Bottom-left
    glVertex2f(0.8, -0.2)  # Bottom-right
    glVertex2f(0.8, -0.8)  # Top-right
    glVertex2f(0.2, -0.8)  # Top-left
    glEnd()

    # Draw a cyan polygon
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Cyan color
    glVertex2f(-0.2, 0.0)  # Point 1
    glVertex2f(0.0, 0.2)   # Point 2
    glVertex2f(0.2, 0.0)   # Point 3
    glVertex2f(0.1, -0.2)  # Point 4
    glVertex2f(-0.1, -0.2) # Point 5
    glEnd()

# Set up OpenGL environment (background color, depth testing, etc.)
def setup():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    glEnable(GL_DEPTH_TEST)  # Enable depth testing (for 3D rendering)
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)  # Orthographic projection (2D)

# Function to handle drawing the primitives
def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear screen and depth buffer
    draw_primitives()  # Draw the primitives
    glfw.swap_buffers(window)  # Swap buffers to display the drawn content

# Main function to create a window, process user input, and render primitives
def main():
    if not glfw.init():
        return

    global window
    window = glfw.create_window(1920, 1080, "2D Drawing", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    setup()  # Set up OpenGL environment

    while not glfw.window_should_close(window):
        draw()  # Draw the primitives
        glfw.poll_events()  # Poll for events

    glfw.terminate()

if __name__ == "__main__":
    main()
