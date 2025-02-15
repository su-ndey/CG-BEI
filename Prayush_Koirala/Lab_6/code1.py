import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Function to draw the primitives
def draw_primitives():
    # Draw a line with width 10
    glLineWidth(10)
    glColor3f(1.0, 1.0, 1.0)  # White color
    glBegin(GL_LINES)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.5, 0.5)
    glEnd()

    # Draw a red rectangle
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glBegin(GL_QUADS)
    glVertex2f(-0.8, -0.1)
    glVertex2f(-0.8, -0.5)
    glVertex2f(-0.4, -0.5)
    glVertex2f(-0.4, -0.1)
    glEnd()

    # Draw a blue rectangle
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glBegin(GL_QUADS)
    glVertex2f(0.4, -0.1)
    glVertex2f(0.4, -0.5)
    glVertex2f(0.8, -0.5)
    glVertex2f(0.8, -0.1)
    glEnd()

    # Draw a cyan polygon
    glColor3f(0.0, 1.0, 1.0)  # Cyan color
    glBegin(GL_POLYGON)
    glVertex2f(0.0, 0.2)
    glVertex2f(-0.2, 0.0)
    glVertex2f(-0.1, -0.3)
    glVertex2f(0.1, -0.3)
    glVertex2f(0.2, 0.0)
    glEnd()

# Set up OpenGL environment
def setup():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)  # Orthographic projection
    glMatrixMode(GL_MODELVIEW)

# Render loop
def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen
    glLoadIdentity()
    draw_primitives()  # Draw the shapes
    glfw.swap_buffers(window)  # Swap buffers to display the drawn content

# Main function
def main():
    if not glfw.init():
        return

    global window
    window = glfw.create_window(800, 600, "OpenGL Primitives", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    setup()

    while not glfw.window_should_close(window):
        draw()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
