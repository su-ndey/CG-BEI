import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_line():
    glLineWidth(10)  # Set the width of the line
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 0.0)  # Red color
    glVertex2f(-0.25, 0.25)
    glVertex2f(0.25, 0.25)
    glEnd()

def draw_rectangle():
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glVertex2f(-0.8, 0.8)
    glVertex2f(-0.4, 0.8)
    glVertex2f(-0.4, 0.4)
    glVertex2f(-0.8, 0.4)
    
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glVertex2f(0.4, 0.8)
    glVertex2f(0.8, 0.8)
    glVertex2f(0.8, 0.4)
    glVertex2f(0.4, 0.4)
    glEnd()

def draw_polygon():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Cyan color
    glVertex2f(-0.6, -0.4)
    glVertex2f(-0.4, -0.8)
    glVertex2f(0.4, -0.8)
    glVertex2f(0.6, -0.4)
    glVertex2f(0.4, 0.0)
    glVertex2f(-0.4, 0.0)
    glEnd()

def setup():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_line()
    draw_rectangle()
    draw_polygon()
    glfw.swap_buffers(window)

def main():
    if not glfw.init():
        return
    global window
    window = glfw.create_window(800, 600, "2D Drawing", None, None)
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
