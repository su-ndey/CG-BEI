import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
# Function to draw a line
def draw_polygon():
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 0.0) # Yellow
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, 10.0) 
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(5.0, 15.0)
    glEnd()

# Set up OpenGL environment (background color, depth testing, etc.)
def setup():
    glClearColor(0.0, 0.0, 0.0, 1.0) # Set background color to black
    glEnable(GL_DEPTH_TEST) # Enable depth testing (for 3D rendering)
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0) # Orthographic projection(2D)
# The function to handle drawing the pixel
def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear screen and depth buffer
    draw_polygon() # Draw the primitive
    glfw.swap_buffers(window)


def main():
    if not glfw.init():
        return

    global window
    window = glfw.create_window(800, 600, "2D Pixel", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    setup()

    while not glfw.window_should_close(window):
        draw() # Draw the pixel
        glfw.poll_events() # Poll for events
    glfw.terminate()
if __name__ == "__main__":
    main()