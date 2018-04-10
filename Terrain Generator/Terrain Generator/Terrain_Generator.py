import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import numpy

vertices = []
edges = []
triangles=[]
Lines=[]
nptx=10
npty=10

#Vertex Coordinate Generator
for ptx in range(0,nptx):
    for pty in range(0,npty):
        ptz=random.random()
        new_vertice=(ptx,ptz,pty)
        vertices.append(new_vertice)

#Triangle Coordinate Generator
for pty in range(0,npty-1):
    for ptx in range(0,nptx):
        top_triangle=(pty*nptx+ptx,pty*nptx+ptx+1,pty*nptx+ptx+nptx)
        bot_triangle=(pty*nptx+ptx+1,pty*nptx+ptx+nptx,pty*nptx+ptx+nptx+1)
        triangles.append(top_triangle)
        triangles.append(bot_triangle)

#horizontal line Coordinate Generator
for pty in range(0,npty):
    for ptx in range(0,nptx-1):
        horz_line=(pty*nptx+ptx,pty*nptx+ptx+1)
        Lines.append(horz_line)

#vertical line Coordinate Generator
for pty in range(0,npty-1):
    for ptx in range(0,nptx):
        vert_line=(ptx+pty*nptx,ptx+nptx+pty*nptx)
        Lines.append(vert_line)

#diagonal line Coordinate Generator
for pty in range(0,npty-1):
    for ptx in range(0,nptx-1):
        cut_line=(ptx+1+pty*nptx,ptx+nptx+pty*nptx)
        Lines.append(cut_line)

modtriangles=triangles[:-1]
vertices_tuple=tuple(vertices)
lines_tuple=tuple(Lines)
triangles_tuple=tuple(modtriangles)
#print(Lines)
#print(triangles_tuple)
#print(vertices_tuple)

def terrain():
    glBegin(GL_LINES)
    for line in lines_tuple:
        for vertex in line:
            glVertex3fv(vertices_tuple[vertex])
    glEnd()

def triangledraw():
    glBegin(GL_LINES)
    for line in lines_tuple:
        for vertex in line:
            glVertex3fv(vertices_tuple[vertex])
    glEnd()
    glBegin(GL_TRIANGLES)
    for triangle in triangles_tuple:
        for vertex in triangle:
            glVertex3fv(vertices_tuple[vertex])
    glEnd()

def main():
    pygame.init()
    display=(800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
   
    gluPerspective(45, (display[0]/display[1]),0.1,200)
    glTranslatef(-5,-5,-20)
    glRotatef(0,0,0,0)

    crashed = False
    x_move=0
    y_move=0

    while not crashed:
        for event in pygame.event.get():
            if pygame.event==pygame.QUIT:
                pygame.quit()
                quit()
           
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_move=0.3
                if event.key==pygame.K_RIGHT:
                    x_move=-0.3
                if event.key==pygame.K_UP:
                    y_move=-0.3
                if event.key==pygame.K_DOWN:
                    y_move=0.3

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_move=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    y_move=0
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==4:
                    glTranslatef(0,0,1.0)
                if event.button==5:
                    glTranslatef(0,0,-1.0)
        glTranslatef(x_move,y_move,0)
        x=glGetDoublev(GL_MODELVIEW_MATRIX)
        camera_x=x[3][0]
        camera_y=x[3][1]
        camera_z=x[3][2]

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        terrain()
        pygame.display.flip()
main()



