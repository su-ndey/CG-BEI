import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Function to draw the hexagon
def draw_primitives():
    # Draw the yellow hexagon
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 0.0)  # Yellow color
    
    # Coordinates for the straight hexagon in clockwise order
    glVertex2f(5.0, 15.0)  # Bottom-left corner
    glVertex2f(0.0, 10.0)  # Bottom-right corner
    glVertex2f(0.0, 5.0) 
    glVertex2f(5.0, 0.0)   # Left-middle
    glVertex2f(10.0, 10.0) # Right-middle
    glVertex2f(10.0, 5.0) 
    glVertex2f(5.0, 0.0)   # Left-middle
    
    glEnd()

# Set up OpenGL environment (background color, depth testing, etc.)
def setup():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    glEnable(GL_DEPTH_TEST)  # Enable depth testing (for 3D rendering)
    
    # Get the window size
    width, height = glfw.get_window_size(window)
    
    # Calculate the aspect ratio of the window
    aspect_ratio = width / float(height)
    
    # Set up the coordinate system with center (0, 0) and the specified range (-10 to 10, -15 to 15)
    # Adjust the projection matrix for the correct aspect ratio
    if aspect_ratio >= 1.0:
        glOrtho(-10.0 * aspect_ratio, 10.0 * aspect_ratio, -15.0, 15.0, -1.0, 1.0)
    else:
        glOrtho(-10.0, 10.0, -15.0 / aspect_ratio, 15.0 / aspect_ratio, -1.0, 1.0)

# Function to handle drawing the primitives
def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear screen and depth buffer
    draw_primitives()  # Draw the hexagon
    glfw.swap_buffers(window)  # Swap buffers to display the drawn content

# Main function to create a window, process user input, and render primitives
def main():
    if not glfw.init():
        return

    global window
    window = glfw.create_window(800, 800, "Yellow Hexagon", None, None)  # Create a window
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)  # Set OpenGL context
    setup()  # Set up OpenGL environment

    while not glfw.window_should_close(window):
        draw()  # Draw the hexagon
        glfw.poll_events()  # Poll for events

    glfw.terminate()

if __name__ == "__main__":
    main()
