import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

def terrain():
    vertices = []
    edges = []
    nptx=10
    npty=10

    for ptx in range(0,nptx):
        for pty in range(0,npty):
            new_vertice=(ptx,pty,0)
            vertices.append(new_vertice)

    for xedge in range(0,(nptx*npty-1)):
        new_edges=(xedge,xedge+1)
        edges.append(new_edges)
    for yedge in range(0,(nptx*npty-nptx)):
        new_edges=(yedge,yedge+nptx)
        edges.append(new_edges)

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display=(800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
   
    gluPerspective(45, (display[0]/display[1]),0.1,200)
    glTranslatef(0.0,0.0,-5)

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if pygame.event==pygame.quit():
                pygame.quit()
                quit()
        terrain()
main()

