from OpenGL.GL import *

def zero(a,b):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 1.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical    
    glVertex2f(a, b)
    glVertex2f(a, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    glVertex2f(s, b)
    glVertex2f(s, x)
    
    glVertex2f(s, z)
    glVertex2f(s, b)

    #horizontal
    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)

    glEnd()


def one(a,b):
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical
    glVertex2f(a, b)
    glVertex2f(a, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    glEnd()

def two(a,b):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical
    glVertex2f(a, b)
    glVertex2f(a, x)

    glVertex2f(s, z)
    glVertex2f(s, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)
   
    glEnd()

def three(a,b):
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    x=b+20
    z=b-20
    s=a-20

    #verticle
    glVertex2f(a, b) 
    glVertex2f(a, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)
   
    glEnd()    

def four(a,b):
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    x=b+20
    z=b-20
    s=a-20

    #verticle
    glVertex2f(a, b) 
    glVertex2f(a, x)

    glVertex2f(s, b)
    glVertex2f(s, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)
   
    glEnd()  

def five(a,b):
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 0.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical
    glVertex2f(s, b)
    glVertex2f(s, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)
   
    glEnd()    

def six(a,b):
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 1.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical
    glVertex2f(s, b)
    glVertex2f(s, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    glVertex2f(s, z)
    glVertex2f(s, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)
   
    glEnd()  

def seven(a,b):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 1.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical
    glVertex2f(a, b)
    glVertex2f(a, x)

    glVertex2f(a, z)
    glVertex2f(a, b)
 
    #horizontal
    glVertex2f(s,x)
    glVertex2f(a,x)
   
    glEnd()

def eight(a,b):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical    
    glVertex2f(a, b)
    glVertex2f(a, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    glVertex2f(s, b)
    glVertex2f(s, x)
    
    glVertex2f(s, z)
    glVertex2f(s, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)

    glEnd()

def nine(a,b):
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 1.0)
    x=b+20
    z=b-20
    s=a-20

    #verticle
    glVertex2f(a, b) 
    glVertex2f(a, x)

    glVertex2f(s, b)
    glVertex2f(s, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)
   
    glEnd()  