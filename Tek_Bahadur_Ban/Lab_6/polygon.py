import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_hexagon():
    glColor3f(1.0,1.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(0.0,5.0)
    glVertex2f(-5.0,2.5)
    glVertex2f(-5.0,-2.5)
    glVertex2f(0.0,-5.0)
    glVertex2f(5.0,-2.5)
    glVertex2f(5.0,2.5)
    glEnd()

def setup():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10.0,10.0,-10.0,10.0,-1.0,1.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_hexagon()
    glfw.swap_buffers(window)

def main():
    if not glfw.init():
        return

    global window
    window = glfw.create_window(800, 600, "Yellow Hexagon", None, None)
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
