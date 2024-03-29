from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from MidPointLine import *
import array as arr

print("Enter your ID: ")
x = input()
arr = [int(x) for x in str(x)]

def iterate():
    glViewport(0, 0, 2000, 2000)#zoom
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
 

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # Drawing the number 0
    # MidpointLine(10, 10, 10, 15)
    # MidpointLine(10, 5, 10, 10)
    # MidpointLine(10, 15, 5, 15)
    # MidpointLine(5, 10, 5, 5)
    # MidpointLine(5, 5, 10, 5) 
    # MidpointLine(5, 10, 5, 15)
    d=1
    f=0
    g=1
    h=2 
    j=len(arr)-2
    z=100
    y=100
    for i in range(2):
        if arr[j]==0:
           zero(y,z,d,f,g,h)
        elif arr[j]==1:
            one(y,z,d,f,g,h) 
        elif arr[j]==2:
            two(y,z,d,f,g,h)     
        elif arr[j]==3:
            three(y,z,d,f,g,h)
        elif arr[j]==4:
            four(y,z,d,f,g,h)
        elif arr[j]==5:
            five(y,z,d,f,g,h)
        elif arr[j]==6:
            six(y,z,d,f,g,h)
        elif arr[j]==7:
            seven(y,z,d,f,g,h)
        elif arr[j]==8:
            eight(y,z,d,f,g,h)
        else:
            nine(y,z,d,f,g,h)      

        y+=30  
        j+=1
    
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700) #window size
glutInitWindowPosition(700, 100)#window position
window = glutCreateWindow(b"500 taka vangti lagbe") #window name
glutDisplayFunc(showScreen)
glutMainLoop()



