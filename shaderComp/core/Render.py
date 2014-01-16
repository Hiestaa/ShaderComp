import OpenGL 
OpenGL.ERROR_ON_COPY = True 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.arrays import vbo
import time
 
# PyOpenGL 3.0.1 introduces this convenience module...
from OpenGL.GL.shaders import *
 
import time, sys
import numpy

from ObjLoader import *

GL_FRAGMENT_SHADER = 0x8B30
GL_VERTEX_SHADER = 0x8B31


class Render :
	def __init__(self):
		self.baseRot = 0.2
		self.rotY = 0
		self.trans = [0.0, 0.0, 0.0]
		self.size = [1.0, 1.0, 1.0]
		self.obj = None

	def initGL(self, Width, Height) : 
		glClearColor(0.0, 0.0, 0.0, 0.0)
		glClearDepth(1.0)
		glShadeModel(GL_SMOOTH)
 
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
		glMatrixMode(GL_MODELVIEW)

	def myCompileProgram(self, vertexSource, fragmentSource):
		program = compileProgram(
			compileShader(vertexSource, GL_VERTEX_SHADER),
			compileShader(fragmentSource, GL_FRAGMENT_SHADER))
		return program
	
	def ReSizeGLScene(self, Width, Height):
		if Height == 0:
			Height = 1
		glViewport(0, 0, Width, Height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
		glMatrixMode(GL_MODELVIEW)
	
	def keyPressed(self, *args):
		# If escape is pressed, kill everything.
		if args[0] == '\x1b':
			sys.exit()
		elif args[0] == 'c':
			self.rotY -= 1
		elif args[0] == 'x':
			self.rotY += 1
		elif args[0] == 'r' :
			self.trans[1] -= 0.1
		elif args[0] == 'f' :
			self.trans[1] += 0.1
		elif args[0] == 'd' :
			self.trans[0] -= 0.1
		elif args[0] == 'a' :
			self.trans[0] += 0.1
		elif args[0] == 'w' :
			self.trans[2] += 0.1
		elif args[0] == 's' :
			self.trans[2] -= 0.1
	
	def baseDemo(self) :
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		
		glTranslatef(self.trans[0], self.trans[1], self.trans[2])
		glScalef(self.size[0], self.size[1], self.size[2])
		
		glTranslatef(0.0, -1.0, -55.0)
		glRotate(self.rotY , 0.0, 1.0, 0.0)
		glutSolidTeapot(7.0)
		glTranslatef(0.0, -1.0, -15.0)
		glutSolidSphere(4.0, 20, 20)
		glTranslatef(0.0, -1.0, -15.0)
		glutSolidCube(5.0)
		glTranslatef(0.0, -1.0, -10.0)
		glutSolidTorus(2.0, 4.0, 10, 10)
		self.rotY += self.baseRot
		
		glScalef(1.0 / self.size[0], 1.0 / self.size[1], 1.0 / self.size[2])
		# Swap buffers
		glutSwapBuffers()
		
	def teaPot(self) :
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glTranslatef(self.trans[0], self.trans[1], self.trans[2])
		glScalef(self.size[0], self.size[1], self.size[2])
		
		glTranslatef(0.0, -1.0, -55.0)
		glRotate(self.rotY , 0.0, 1.0, 0.0)
		glutSolidTeapot(7.0)
		self.rotY += self.baseRot
		# Swap buffers
		glutSwapBuffers()
		
	def sphere(self) :
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glTranslatef(self.trans[0], self.trans[1], self.trans[2])
		glScalef(self.size[0], self.size[1], self.size[2])
		
		glTranslatef(0.0, -1.0, -55.0)
		glRotate(self.rotY , 0.0, 1.0, 0.0)
		glutSolidSphere(4.0, 20, 20)
		self.rotY += self.baseRot
		
		glScalef(1.0 / self.size[0], 1.0 / self.size[1], 1.0 / self.size[2])
		# Swap buffers
		glutSwapBuffers()
		
	def cube(self) :
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glTranslatef(self.trans[0], self.trans[1], self.trans[2])
		glScalef(self.size[0], self.size[1], self.size[2])
		
		glTranslatef(0.0, -1.0, -55.0)
		glRotate(self.rotY , 0.0, 1.0, 0.0)
		glutSolidCube(5.0)
		self.rotY += self.baseRot
		
		glScalef(1.0 / self.size[0], 1.0 / self.size[1], 1.0 / self.size[2])
		# Swap buffers
		glutSwapBuffers()
		
	def torus(self) :
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glTranslatef(self.trans[0], self.trans[1], self.trans[2])
		glScalef(self.size[0], self.size[1], self.size[2])
		
		glTranslatef(0.0, -1.0, -55.0)
		glRotate(self.rotY , 0.0, 1.0, 0.0)
		glutSolidTorus(2.0, 4.0, 10, 10)
		self.rotY += self.baseRot
		
		glScalef(1.0 / self.size[0], 1.0 / self.size[1], 1.0 / self.size[2])
		# Swap buffers
		glutSwapBuffers()
	 
	
	def model(self) :
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glTranslatef(self.trans[0], self.trans[1], self.trans[2])
		glScalef(self.size[0], self.size[1], self.size[2])
		print self.size[0], self.size[1], self.size[2]
		
		glTranslatef(0.0, -1.0, -20.0)
		glRotate(self.rotY , 0.0, 1.0, 0.0)
		
		vertices = (0, self.obj.vboPosColorTextureNormal)
		if vertices[1] == None :
			vertices = (1, self.obj.vboPosColorTexture)
		if vertices[1] == None :
			vertices = (2, self.obj.vboPosColorNormal)
		if vertices[1] == None :
			vertices = (3, self.obj.vboPosColor)
		
		
		vertexPositions = vbo.VBO(vertices[1])
		vertexPositions.bind()

		glEnableClientState(GL_VERTEX_ARRAY)
		glEnableClientState(GL_COLOR_ARRAY)
		if vertices[0] == 0 or vertices[0] == 1:
			glEnableClientState(GL_TEXTURE_COORD_ARRAY)
		if vertices[0] == 0 or vertices[0] == 2:
			glEnableClientState(GL_NORMAL_ARRAY)
			
		
		if vertices[0] == 0 :
			glVertexPointer(3, GL_FLOAT, 48, vertexPositions)
			glColorPointer(3, GL_FLOAT, 48, vertexPositions+12)
			glTexCoordPointer(2, GL_FLOAT, 48, vertexPositions+24)
			glNormalPointer(GL_FLOAT, 48, vertexPositions+36)
			glDrawArrays(GL_TRIANGLES, 0, vertices[1].shape[0]);
		elif vertices[0] == 1 :
			glVertexPointer(3, GL_FLOAT, 36, vertexPositions)
			glColorPointer(3, GL_FLOAT, 36, vertexPositions+12)
			glTexCoordPointer(2, GL_FLOAT, 36, vertexPositions+24)
			glDrawArrays(GL_TRIANGLES, 0,  vertices[1].shape[0]);
		elif vertices[0] == 2 :
			glVertexPointer(3, GL_FLOAT, 36, vertexPositions)
			glColorPointer(3, GL_FLOAT, 36, vertexPositions+12)
			glNormalPointer(GL_FLOAT, 36, vertexPositions+24)
			glDrawArrays(GL_TRIANGLES, 0,  vertices[1].shape[0]);
		elif vertices[0] == 3 :
			glVertexPointer(3, GL_FLOAT, 24, vertexPositions)
			glColorPointer(3, GL_FLOAT, 24, vertexPositions+12)
			glDrawArrays(GL_TRIANGLES, 0, vertices[1].shape[0]);
		
		
		vertexPositions.unbind()
		glDisableClientState(GL_VERTEX_ARRAY)
		glDisableClientState(GL_COLOR_ARRAY)
		glDisableClientState(GL_TEXTURE_COORD_ARRAY)
		glDisableClientState(GL_NORMAL_ARRAY)
		
		glScalef(1.0 / self.size[0], 1.0 / self.size[1], 1.0 / self.size[2])
		self.rotY += self.baseRot
		
		# Swap buffers
		glutSwapBuffers()
	
	def loadModel(self, modelName) :
		print 'Load Model :', modelName
		objloader = ObjLoader()
		self.obj = objloader.load(modelName)
		
		texdata = self.obj.texture
		if texdata != None :
			glEnable(GL_TEXTURE_2D)
			texture=glGenTextures(1)
			glBindTexture( GL_TEXTURE_2D, texture);
			
			
			glTexEnvf( GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE );
			glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S,
							 GL_REPEAT);
			glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T,
							 GL_REPEAT );
			
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

			glTexImage2Df(GL_TEXTURE_2D, 0, 4, 0, GL_RGBA, texdata)
			
			
			glBindTexture( GL_TEXTURE_2D, texture );
		
	def execute(self, progs, type, size, rot, modelName) :
		self.baseRot = rot
		self.size = size
		glutInit()
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
		glutInitWindowSize(1200, 800)
		glutInitWindowPosition(0, 0)
		window = glutCreateWindow("Render")  
		glutReshapeFunc(self.ReSizeGLScene)
		glutKeyboardFunc(self.keyPressed)
		
		if  type == 'model' :
			self.loadModel(modelName)
			glutDisplayFunc(self.model)
			glutIdleFunc(self.model)
		elif type == 'teapot' :
			glutDisplayFunc(self.teaPot)
			glutIdleFunc(self.teaPot)
		elif type == 'sphere' :
			glutDisplayFunc(self.sphere)
			glutIdleFunc(self.sphere)
		elif type == 'cube' :
			glutDisplayFunc(self.cube)
			glutIdleFunc(self.cube)
		elif type == 'torus' :
			glutDisplayFunc(self.torus)
			glutIdleFunc(self.torus)
		else :
			glutDisplayFunc(self.baseDemo)
			glutIdleFunc(self.baseDemo)
			
		self.initGL(800, 600)
		
		program = self.myCompileProgram(progs[0], progs[1])
		glUseProgram(program)
		
		glEnable(GL_DEPTH_TEST);
		glutMainLoop()
