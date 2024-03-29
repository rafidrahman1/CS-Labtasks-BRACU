from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Numbers import *
import random
import array as arr

print("Enter your ID: ")
x = input()
arr = [int(x) for x in str(x)]

def draw_points(x, y, a, b, c):
    glPointSize(2) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(a, b, c) #color
    glVertex2f(x,y) #jekhane show korbe pixel, Cordinates
    glEnd()

def draw_hlines(x1,x2,y):
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(x1,y)
    glVertex2f(x2,y)
    glEnd()


def draw_vlines(x,y1,y2):
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(x,y1)
    glVertex2f(x,y2)
    glEnd()

def draw_lines(a,b,c,d):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(a, b)
    glVertex2f(c, d)
    glEnd()

#def one(x,y):
#def triangles()
    #glBegin(GL_TRIANGLES)

    #glEnd()s

def iterate():
    glViewport(0, 0, 700, 700)#zoom
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #konokichur color set (RGB)
    #call the draw methods here
    #draw_points(100, 100)
    draw_hlines(150,250, 150)#outer wall(S)
    draw_hlines(150,250,250)#outer wall(N)
    draw_vlines(150, 150, 251)#outer wall(W)
    draw_vlines(250, 150, 250)#outer wall(E)
    draw_lines(150,250,200,325)#(L roof)
    draw_lines(250,250, 200,325)#(R roof)

    #draw_window
    draw_hlines(155,185, 210)#outer wall(S)
    draw_hlines(154,185,240)#outer wall(N)
    draw_vlines(155, 210, 240)#outer wall(W)
    draw_vlines(185, 210, 240)#outer walla(E)

    draw_hlines(215,245, 210)#outer wall(S)
    draw_hlines(214,245,240)#outer wall(N)
    draw_vlines(215, 210, 240)#outer wall(W)
    draw_vlines(245, 210, 240)#outer wall(E)

    #draw_door
    draw_hlines(184,215, 200)#outer wall(N)
    draw_vlines(185, 150, 200)#outer wall(W)
    draw_vlines(215, 150, 200)#outer wall(E)

    #door_knob
    draw_points(210, 175, 1, 0, 1)

    ###################
    #random pixel Generator.
    
    for i in range(50):
     n = random.randint(300,400)#random x axis point
     p = random.randint(300,400)#random y axis point
     a = random.randint(0,1)#radom color
     b = random.randint(0,1)
     c = random.randint(0,1)
     draw_points(n,p,a,b,c)
     

    
    #student ID generator
    #2
    """
    draw_vlines(285, 210, 230)
    draw_vlines(265, 190, 210)
    draw_hlines(265,285,210)
    draw_hlines(265,285,190)
    draw_hlines(265,285,230)
    """
    z=230
    y=285
    for i in range(len(arr)):
        if arr[i]==0:
           zero(y,z)
        elif arr[i]==1:
            one(y,z) 
        elif arr[i]==2:
            two(y,z)     
        elif arr[i]==3:
            three(y,z)
        elif arr[i]==4:
            four(y,z)
        elif arr[i]==5:
            five(y,z)
        elif arr[i]==6:
            six(y,z)
        elif arr[i]==7:
            seven(y,z)
        elif arr[i]==8:
            eight(y,z)
        else:
            nine(y,z)      

        y+=30             

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800) #window size
glutInitWindowPosition(500, 125)#window position
window = glutCreateWindow(b"500 taka vangti lagbe") #window name
glutDisplayFunc(showScreen)
glutMainLoop()

