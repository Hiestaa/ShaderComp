#! /usr/bin/env python
'''
Quaint little Python/OpenGL/Shader example
 
Uses the x-ray shader found in MeshLab
 
Code is a slightly modified version of http://www.pygame.org/wiki/GLSLExample
'''
import OpenGL 
OpenGL.ERROR_ON_COPY = True 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 
# PyOpenGL 3.0.1 introduces this convenience module...
from OpenGL.GL.shaders import *
 
import time, sys
program = None
global falloffValue
global rotX
global rotY
global rotZ
 
# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):                # We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)    # This Will Clear The Background Color To Black
    glClearDepth(1.0)                    # Enables Clearing Of The Depth Buffer
    glShadeModel(GL_SMOOTH)                # Enables Smooth Color Shading
 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                    # Reset The Projection Matrix
                                        # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
 
    glMatrixMode(GL_MODELVIEW)
 

def buildProgram(progs) :
	if not glUseProgram:
		print 'Missing Shader Objects!'
		sys.exit(1)
		
	global program
	if progs[0] != '' and progs[1] != '' :
		program = compileProgram(
			compileShader(progs[0] ,GL_VERTEX_SHADER),
			compileShader(progs[1] ,GL_FRAGMENT_SHADER),
		)
	else :
		if progs[0] != '':
			program = compileProgram(
				compileShader(progs[0] ,GL_VERTEX_SHADER),
			)
		if progs[1] != '':
			program = compileProgram(
				compileShader(progs[1] ,GL_FRAGMENT_SHADER),
			)
 
# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:                        # Prevent A Divide By Zero If The Window Is Too Small 
        Height = 1
 
    glViewport(0, 0, Width, Height)        # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
 
# The main drawing function. 
def DrawGLScene():
	global rotX
	global rotY
	global rotZ
	# Clear The Screen And The Depth Buffer
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()                    # Reset The View 
 
 
	# Move Left 1.5 units and into the screen 6.0 units.
	glTranslatef(0.0, 0.0, -6.0)
 
	# Spin this business.
	glRotatef(rotX,1.0,0.0,0.0)
	glRotatef(rotY,0.0,1.0,0.0)
	glRotatef(rotZ,0.0,0.0,1.0)
 
	# Load something with some curves
	glutSolidTeapot(1.0)
 
	# Enable blending and disable depth masking (x-ray shader only applies the opacity falloff.
	glEnable(GL_BLEND);
	glDepthMask(GL_FALSE);
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
 
	
 
	# Include a lovely dodecahedron
	glScalef(0.3,0.3,0.3)
	glutSolidDodecahedron()
 
	# Swap buffers
	glutSwapBuffers()
 
# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
	global rotX
	global rotY
	global rotZ
	# If escape is pressed, kill everything.
	if args[0] == '\x1b':
		sys.exit()
	elif args[0] == 'c':
		rotX -= 5
	elif args[0] == 'x':
		rotX += 5
	elif args[0] == 'v':
		rotY -= 5
	elif args[0] == 'b':
		rotY += 5
	elif args[0] == 'n':
		rotZ -= 5
	elif args[0] == 'm':
		rotZ += 5
 
def main(progs):
	global window
	global rotX
	global rotY
	global rotZ
 
	# For now we just pass glutInit one empty argument. I wasn't sure what should or could be passed in (tuple, list, ...)
	# Once I find out the right stuff based on reading the PyOpenGL source, I'll address this.
	glutInit(sys.argv)
 
	# Select type of Display mode:   
	#  Double buffer 
	#  RGBA color
	# Alpha components supported 
	# Depth buffer
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
 
	# get a 640 x 480 window 
	glutInitWindowSize(640, 480)
 
	# the window starts at the upper left corner of the screen 
	glutInitWindowPosition(0, 0)
 
	# Okay, like the C version we retain the window id to use when closing, but for those of you new
	# to Python (like myself), remember this assignment would make the variable local and not global
	# if it weren't for the global declaration at the start of main.
	window = glutCreateWindow("ShaderComp")
 
	# Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
	# set the function pointer and invoke a function to actually register the callback, otherwise it
	# would be very much like the C version of the code.    
	glutDisplayFunc(DrawGLScene)
 
	# Uncomment this line to get full screen.
	#glutFullScreen()
 
	# When we are doing nothing, redraw the scene.
	glutIdleFunc(DrawGLScene)
 
	# Register the function called when our window is resized.
	glutReshapeFunc(ReSizeGLScene)
 
	# Register the function called when the keyboard is pressed.  
	glutKeyboardFunc(keyPressed)
 
	# Initialize our window. 
	InitGL(800, 600)
	buildProgram(progs)
 
	#Start using our program
	glUseProgram(program)
 
	#Set defaults
	rotX = 0.0
	rotY = 0.0
	rotZ = 0.0
 
	#glEnable (GL_BLEND)
	#glBlendFunc (GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
 
	# Start Event Processing Engine    
	glutMainLoop()
	
class Render :
	def __init__(self):
		pass
		
	def execute(self, progs) :
		print "Hit ESC key to quit."
		print "x - increase Rotate"
		print "c - decrease Rotate"
		main(progs)
		