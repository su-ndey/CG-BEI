import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
def draw_line():
    glLineWidth(10.0) # Set line width
    glBegin(GL_LINES)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(-0.5,-0.5)
    glVertex2f(0.5,0.5)
    glEnd()

def setup():
    glClearColor(0.0,0.0,0.0,1.0)
    glEnable(GL_DEPTH_TEST)
    glOrtho(-1.0,1.0,-1.0,1.0,-1.0,1.0)
def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_line()
    glfw.swap_buffers(window)
def main():
    if not glfw.init():
        return
    global window
    window=glfw.create_window(800,600,"2D Pixel",None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    setup()

    while not glfw.window_should_close(window):
        draw()
        glfw.poll_events()
    glfw.terminate()
if __name__=="__main__":
    main()