import random
from random import randint
from random import seed

from OpenGL.GL import *
from OpenGL.GLUT import *


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
def draw_point():
    glPointSize(5)
    glBegin(GL_POINTS)
    x = 1
    y = 3
    for i in range(50):
        glVertex2f(x, y)
        x += 10
        y += 10
    glEnd()

def showScreen():
    glLoadIdentity()
    iterate()
    glColor3f(3.0, 2.0, 4.0)
    #call the draw methods here

    draw_point()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 1")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
