import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define the hexagon's coordinates
vertices = [
    (0, 5),
    (5, 0),
    (5, -5),
    (0, -10),
    (-5, -5),
    (-5, 0)
]

def draw_hexagon():
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0) 
    glColor3f(1.0, 1.0, 0.0)  
    glPointSize(5) 
    glOrtho(-10, 10, -10, 10, -1, 1)
    
def main():
    if not glfw.init():
        return
    global window
    window = glfw.create_window(800, 600, "2D Drawing", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    init()

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)  
        draw_hexagon()  
        glfw.swap_buffers(window)  
        glfw.poll_events() 
    glfw.terminate()
    
if __name__ == "__main__":
    main()
