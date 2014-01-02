from ctypes import *
import sys
 
import pygame
from pygame.locals import *
 
import OpenGL.GL as gl
 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL.shaders import *
 
glCompileShader = gl.glCompileShader
glUseProgram = gl.glUseProgram

 
GL_FRAGMENT_SHADER = 0x8B30
GL_VERTEX_SHADER = 0x8B31


var1Value = 0.0
var2Value = 0.0
program = None


def mod_var1(val):
	global var1Value
	if program:
		var1 = glGetUniformLocation(program, "var1")
		if not var1 in (None,-1):
			var1Value = var1Value + val
			glUniform1f(var1, var1Value)
			print "var1=", var1Value

def mod_var2(val):
	global var2Value
	if program:
		var2 = glGetUniformLocation(program, "var2")
		if not var2 in (None,-1):
			var2Value = var2Value + val
			glUniform1f(var2, var2Value)
			print "var2=", var2Value

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
 
	# If escape is pressed, kill everything.
	if args[0] == '\x1b':
		sys.exit()
	elif args[0] == 'q':
		print "Decreasing var1",
		mod_var1(0.1)
	elif args[0] == 'd':
		print "Increasing var1",
		mod_var1(-0.1)
	elif args[0] == 'z':
		print "Decreasing var2",
		mod_var2(0.1)
	elif args[0] == 's':
		print "Increasing var2",
		mod_var2(-0.1)


def compile_shader(source, shader_type):
	shader = glCompileShader(source, shader_type)
	
	return shader
 
def compile_program(vertex_source, fragment_source):
	vertex_shader = None
	fragment_shader = None

	program = compileProgram(
		compileShader(vertex_source,GL_VERTEX_SHADER), 
		compileShader(fragment_source,GL_FRAGMENT_SHADER))
	return program
 
def load_shader(filename):
	f = open(filename, 'r')
	return f.read()


def main(progs):
	global program
	glutInit(sys.argv)
	width, height = 1024, 768
	pygame.init()
	pygame.display.set_mode((width, height), OPENGL | DOUBLEBUF)
 
	program = compile_program(progs[0], progs[1])
	glUseProgram(program)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(90.0, width/float(height), 1.0, 1000.0)
	glMatrixMode(GL_MODELVIEW)
	glEnable(GL_DEPTH_TEST)
	# Register the function called when the keyboard is pressed.  
	#glutKeyboardFunc(keyPressed)
	
	quit = False
	angle = 0

	mod_var1(1)
	mod_var2(2)


	while not quit:
		for e in pygame.event.get():
			if e.type in (QUIT, KEYDOWN):
				quit = True
		#glClearColor(1,1,1,1)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glTranslatef(0.0, -1.0, -55.0)
		glRotate(angle, 0.0, 1.0, 0.0)
		glUseProgram(program)
		glutSolidTeapot(7.0)
		glTranslatef(0.0, -1.0, -15.0)
		glutSolidSphere(4.0, 20, 20)
		glTranslatef(0.0, -1.0, -15.0)
		glutSolidCube(5.0)
		glTranslatef(0.0, -1.0, -10.0)
		glutSolidTorus(2.0, 4.0, 10, 10)
		angle += 0.2
		pygame.display.flip()

class Render :
	def __init__(self):
		pass
		
	def execute(self, progs) :
		print "Hit ESC key to quit."
		print "x - increase Rotate"
		print "c - decrease Rotate"
		main(progs)
		