import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define the hexagon's coordinates
vertices = [
    (0, 5),
    (5, 0),
    (10, 5),
    (10, 10),
    (5, 15),
    (0, 10)
]

def draw_hexagon():
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white
    glColor(1.0, 1.0, 0.0)  # Set drawing color to black
    glPointSize(5)  # Set point size for vertices
    glOrtho(-20, 20, -20, 20, -1, 1)  # Set orthographic projection

def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    init()
    
    # Main rendering loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT)
        draw_hexagon()
        pygame.display.flip()

if __name__ == "__main__":
    main()
