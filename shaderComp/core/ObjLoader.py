import re
import numpy
import cv2
import math

import OpenGL 
OpenGL.ERROR_ON_COPY = True 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.arrays import vbo
 
# PyOpenGL 3.0.1 introduces this convenience module...
from OpenGL.GL.shaders import *

class Material :
	def __init__(self, name, Ns, Ka, Kd, Ks, Ni, d, illum, mapKa, mapKd, mapKs, mapNs, mapd) :
		self.name = name
		self.Ns = Ns
		self.Ka = numpy.array(Ka, dtype=numpy.float32)
		self.Kd = numpy.array(Kd, dtype=numpy.float32)
		self.Ks = numpy.array(Ks, dtype=numpy.float32)
		self.Ni = Ni
		self.d = d
		self.illum = illum
		self.mapKa = mapKa
		self.mapKd = mapKd
		self.mapKs = mapKs
		self.mapNs = mapNs
		self.mapd = mapd
		
	def matPrint(self) :
		print 'name:', self.name, 'Ns:', self.Ns, 'Ka:', self.Ka, 'Kd:', self.Kd, 'Ks:', self.Ks,
		print 'Ni:', self.Ni, 'd:', self.d, 'illum:', self.illum, 'mapKa:', self.mapKa, 'mapKd:', self.mapKd,
		print 'mapKs:', self.mapKs, 'mapNs:', self.mapNs, 'mapd:', self.mapd

class OBJ :
	def __init__(self, vboList) :
		self.vboList = vboList
		
		self.textures = {}
		maxwidth = 0
		maxheight = 0
		count = 0
		
		for vbo in self.vboList :
			if vbo.material.mapKd not in self.textures and vbo.material.mapKd != None:
				tmp = cv2.imread(vbo.material.mapKd, cv2.IMREAD_COLOR)
				if tmp == None :
					print 'Error: texture not found !', vbo.material.mapKd
					print tmp
					continue
				self.textures[vbo.material.mapKd] = tmp
				if self.textures[vbo.material.mapKd].shape[0] > maxwidth :
					maxwidth = self.textures[vbo.material.mapKd].shape[0]
				if self.textures[vbo.material.mapKd].shape[1] > maxheight :
					maxheight = self.textures[vbo.material.mapKd].shape[1]
				count += 1
				
		self.texture = None
		if count > 0 :
			print count
			self.tabSize = float(int(math.sqrt(count) + 1))
			if count == 1 :
				self.tabSize = 1.0
			print self.tabSize
			
			if maxwidth > maxheight :
				self.maxLen = maxwidth
			else :
				self.maxLen = maxheight
			print 'maLen:', self.maxLen
			self.texture = numpy.empty([self.tabSize * self.maxLen, self.tabSize * self.maxLen, 4], dtype=numpy.float32)
			
			# print self.texture.shape
			# exit()
			
			xPlus = 0
			yPlus = 0
			self.idDict = {}
			for key, value in self.textures.items() :
				print key
				for i in xrange(value.shape[0]) :
					for j in xrange(value.shape[1]) :
						for k in xrange(self.texture.shape[2]) :
							if k == self.texture.shape[2] - 1 :
								self.texture[i + xPlus][j + yPlus][k] = 1
							else :
								self.texture[i + xPlus][j + yPlus][k] = value[i][j][2 - k] / 255.0
				self.idDict[key] = (float(xPlus) / float(self.maxLen), float(yPlus) / float(self.maxLen))
				if xPlus < self.tabSize * self.maxLen :
					xPlus += self.maxLen
				if xPlus >= self.tabSize * self.maxLen:
					xPlus = 0
					yPlus += self.maxLen
		
		# tmp = cv2.imread(self.vboList[0].material.mapKd, cv2.IMREAD_COLOR)
		# tmplen = tmp.shape[0]
		# self.texture = numpy.empty([tmplen * 3, tmp.shape[1], tmp.shape[2] + 1], dtype=numpy.float32)
		# for i in xrange(tmplen) :
			# for j in xrange(self.texture.shape[1]) :
				# for k in xrange(self.texture.shape[2]) :
					# if k == self.texture.shape[2] - 1 :
						# self.texture[i][j][k] = 1
					# else :
						# self.texture[i][j][k] = tmp[i][j][2 - k] / 255.0
		# tmp = cv2.imread(self.vboList[25].material.mapKd, cv2.IMREAD_COLOR)
		# for i in xrange(tmplen) :
			# for j in xrange(self.texture.shape[1]) :
				# for k in xrange(self.texture.shape[2]) :
					# if k == self.texture.shape[2] - 1 :
						# self.texture[i + tmplen][j][k] = 1
					# else :
						# self.texture[i + tmplen][j][k] = tmp[i][j][2 - k] / 255.0
		# tmp = cv2.imread(self.vboList[10].material.mapKd, cv2.IMREAD_COLOR)
		# for i in xrange(tmplen) :
			# for j in xrange(self.texture.shape[1]) :
				# for k in xrange(self.texture.shape[2]) :
					# if k == self.texture.shape[2] - 1 :
						# self.texture[i + tmplen * 2][j][k] = 1
					# else :
						# self.texture[i + tmplen * 2][j][k] = tmp[i][j][2 - k] / 255.0
						
		# print self.texture
		# exit()
		
		self.vboPosColor = None
		self.buildVBOPosColor()
		
		self.vboPosColorNormal = None
		self.buildVBOPosColorNormal()
		
		self.vboPosColorTexture = None
		self.buildVBOPosColorTexture()
		
		self.vboPosColorTextureNormal = None
		self.buildVBOPosColorTextureNormal()
		
		
	def buildVBOPosColor(self) :
		count = 0
		for vbo in self.vboList :
			count += vbo.posColorBuffer.shape[0]
		self.vboPosColor = numpy.empty([count, 6], dtype=numpy.float32)
		i = 0
		for vbo in self.vboList :
			for j in xrange(vbo.posColorBuffer.shape[0]) :
				self.vboPosColor[i][0] = vbo.posColorBuffer[j][0]
				self.vboPosColor[i][1] = vbo.posColorBuffer[j][1]
				self.vboPosColor[i][2] = vbo.posColorBuffer[j][2]
				self.vboPosColor[i][3] = vbo.posColorBuffer[j][3]
				self.vboPosColor[i][4] = vbo.posColorBuffer[j][4]
				self.vboPosColor[i][5] = vbo.posColorBuffer[j][5]
				i += 1

	def buildVBOPosColorNormal(self) :
		count = 0
		for vbo in self.vboList :
			if vbo.posColorNormalBuffer == None :
				return
			count += vbo.posColorNormalBuffer.shape[0]
		self.vboPosColorNormal = numpy.empty([count, 9], dtype=numpy.float32)
		i = 0
		for vbo in self.vboList :
			for j in xrange(vbo.posColorNormalBuffer.shape[0]) :
				self.vboPosColorNormal[i][0] = vbo.posColorNormalBuffer[j][0]
				self.vboPosColorNormal[i][1] = vbo.posColorNormalBuffer[j][1]
				self.vboPosColorNormal[i][2] = vbo.posColorNormalBuffer[j][2]
				self.vboPosColorNormal[i][3] = vbo.posColorNormalBuffer[j][3]
				self.vboPosColorNormal[i][4] = vbo.posColorNormalBuffer[j][4]
				self.vboPosColorNormal[i][5] = vbo.posColorNormalBuffer[j][5]
				self.vboPosColorNormal[i][6] = vbo.posColorNormalBuffer[j][6]
				self.vboPosColorNormal[i][7] = vbo.posColorNormalBuffer[j][7]
				self.vboPosColorNormal[i][8] = vbo.posColorNormalBuffer[j][8]
				i += 1
				
	def buildVBOPosColorTexture(self) :
		count = 0
		for vbo in self.vboList :
			if vbo.posColorTextureBuffer == None :
				return
			count += vbo.posColorTextureBuffer.shape[0]
		self.vboPosColorTexture = numpy.empty([count, 9], dtype=numpy.float32)
		i = 0
		for vbo in self.vboList :
			for j in xrange(vbo.posColorTextureBuffer.shape[0]) :
				self.vboPosColorTexture[i][0] = vbo.posColorTextureBuffer[j][0]
				self.vboPosColorTexture[i][1] = vbo.posColorTextureBuffer[j][1]
				self.vboPosColorTexture[i][2] = vbo.posColorTextureBuffer[j][2]
				self.vboPosColorTexture[i][3] = vbo.posColorTextureBuffer[j][3]
				self.vboPosColorTexture[i][4] = vbo.posColorTextureBuffer[j][4]
				self.vboPosColorTexture[i][5] = vbo.posColorTextureBuffer[j][5]
				# if vbo.material.mapKd == 'maps\cs_italy_texture_0.jpg' :
					# print vbo.material.mapKd
					# print self.idDict[vbo.material.mapKd][0]
					# print self.idDict[vbo.material.mapKd][1]
					# print (((vbo.posColorTextureBuffer[j][6] / self.tabSize) / self.maxLen) * self.textures[vbo.material.mapKd].shape[0]) + ((1.0 / self.tabSize) * self.idDict[vbo.material.mapKd][1])
					# print (((vbo.posColorTextureBuffer[j][7] / self.tabSize) / self.maxLen) * self.textures[vbo.material.mapKd].shape[1]) + ((1.0 / self.tabSize) * self.idDict[vbo.material.mapKd][0])
				if vbo.material.mapKd in self.textures :
					self.vboPosColorTexture[i][6] = (((vbo.posColorTextureBuffer[j][6] / self.tabSize) / self.maxLen) * self.textures[vbo.material.mapKd].shape[0]) + ((1.0 / self.tabSize) * self.idDict[vbo.material.mapKd][1])
					self.vboPosColorTexture[i][7] = (((vbo.posColorTextureBuffer[j][7] / self.tabSize) / self.maxLen) * self.textures[vbo.material.mapKd].shape[1]) + ((1.0 / self.tabSize) * self.idDict[vbo.material.mapKd][0])
				else :
					self.vboPosColorTexture[i][6] = 0
					self.vboPosColorTexture[i][7] = 0
				self.vboPosColorTexture[i][8] = vbo.posColorTextureBuffer[j][8]
				i += 1
				
	def buildVBOPosColorTextureNormal(self) :
		count = 0
		for vbo in self.vboList :
			if vbo.posColorTextureNormalBuffer == None :
				return
			count += vbo.posColorTextureNormalBuffer.shape[0]
		self.vboPosColorTextureNormal = numpy.empty([count, 12], dtype=numpy.float32)
		i = 0
		for vbo in self.vboList :
			for j in xrange(vbo.posColorTextureNormalBuffer.shape[0]) :
				self.vboPosColorTextureNormal[i][0] = vbo.posColorTextureNormalBuffer[j][0]
				self.vboPosColorTextureNormal[i][1] = vbo.posColorTextureNormalBuffer[j][1]
				self.vboPosColorTextureNormal[i][2] = vbo.posColorTextureNormalBuffer[j][2]
				self.vboPosColorTextureNormal[i][3] = vbo.posColorTextureNormalBuffer[j][3]
				self.vboPosColorTextureNormal[i][4] = vbo.posColorTextureNormalBuffer[j][4]
				self.vboPosColorTextureNormal[i][5] = vbo.posColorTextureNormalBuffer[j][5]
				# print self.idDict[vbo.material.mapKd][0], self.idDict[vbo.material.mapKd][1]
				# if vbo.material.mapKd == 'maps\cs_italy_texture_64.jpg' :
					# print self.idDict[vbo.material.mapKd]
				# print (((vbo.posColorTextureNormalBuffer[j][6] / self.tabSize) / self.maxLen) * self.textures[vbo.material.mapKd].shape[0]) + ((1.0 / self.tabSize) * self.idDict[vbo.material.mapKd][0])
				# print (((vbo.posColorTextureNormalBuffer[j][7] / self.tabSize) / self.maxLen) * self.textures[vbo.material.mapKd].shape[1]) + ((1.0 / self.tabSize) * self.idDict[vbo.material.mapKd][1])
				if vbo.material.mapKd in self.textures :
					self.vboPosColorTextureNormal[i][6] = (((vbo.posColorTextureNormalBuffer[j][6] / self.tabSize) / self.maxLen) * self.textures[vbo.material.mapKd].shape[0]) + ((1.0 / self.tabSize) * self.idDict[vbo.material.mapKd][1])
					self.vboPosColorTextureNormal[i][7] = (((vbo.posColorTextureNormalBuffer[j][7] / self.tabSize) / self.maxLen) * self.textures[vbo.material.mapKd].shape[1]) + ((1.0 / self.tabSize) * self.idDict[vbo.material.mapKd][0])
				else :
					self.vboPosColorTextureNormal[i][6] = 0
					self.vboPosColorTextureNormal[i][7] = 0
				self.vboPosColorTextureNormal[i][8] = vbo.posColorTextureNormalBuffer[j][8]
				self.vboPosColorTextureNormal[i][9] = vbo.posColorTextureNormalBuffer[j][9]
				self.vboPosColorTextureNormal[i][10] = vbo.posColorTextureNormalBuffer[j][10]
				self.vboPosColorTextureNormal[i][11] = vbo.posColorTextureNormalBuffer[j][11]
				i += 1
		

class MyVBO :
	def __init__(self, positionVbo, textureVbo, normalVbo, material) :
		self.positionVbo = positionVbo
		self.textureVbo = textureVbo
		self.normalVbo = normalVbo
		self.material = material
		# self.color = None
		# self.buildColor()
		self.posColorBuffer = None
		self.buildPosColorBuffer()
		
		self.posColorNormalBuffer = None
		if self.normalVbo.shape[0] == self.positionVbo.shape[0] :
			self.buildPosColorNormalBuffer()
			
		self.posColorTextureBuffer = None
		if self.textureVbo.shape[0] == self.positionVbo.shape[0] :
			self.buildPosColorTextureBuffer()
			
		self.posColorTextureNormalBuffer = None
		if self.textureVbo.shape[0] == self.positionVbo.shape[0] and self.normalVbo.shape[0] == self.positionVbo.shape[0] :
			self.buildPosColorTextureNormalBuffer()
			
		# tmp = cv2.imread(self.material.mapKd, cv2.IMREAD_COLOR)
		# self.texture = numpy.empty([tmp.shape[0], tmp.shape[1], tmp.shape[2] + 1], dtype=numpy.float32)
		# for i in xrange(self.texture.shape[0]) :
			# for j in xrange(self.texture.shape[1]) :
				# for k in xrange(self.texture.shape[2]) :
					# if k == self.texture.shape[2] - 1 :
						# self.texture[i][j][k] = 1
					# else :
						# self.texture[i][j][k] = tmp[i][j][k] / 255.0
		
		
	def buildColor(self) :
		self.color = numpy.empty(self.positionVbo.shape, dtype=numpy.float32)
		for i in xrange(self.color.shape[0]) :
			self.color[i][0] = self.material.Kd[0]
			self.color[i][1] = self.material.Kd[1]
			self.color[i][2] = self.material.Kd[2]
			
	def buildPosColorBuffer(self) :
		self.posColorBuffer = numpy.empty([self.positionVbo.shape[0], 6], dtype=numpy.float32)
		for i in xrange(self.positionVbo.shape[0]) :
			self.posColorBuffer[i][0] = self.positionVbo[i][0]
			self.posColorBuffer[i][1] = self.positionVbo[i][1]
			self.posColorBuffer[i][2] = self.positionVbo[i][2]
			self.posColorBuffer[i][3] = self.material.Kd[0]
			self.posColorBuffer[i][4] = self.material.Kd[1]
			self.posColorBuffer[i][5] = self.material.Kd[2]
			
	def buildPosColorNormalBuffer(self) :
		self.posColorNormalBuffer = numpy.empty([self.positionVbo.shape[0], 9], dtype=numpy.float32)
		for i in xrange(self.positionVbo.shape[0]) :
			self.posColorNormalBuffer[i][0] = self.positionVbo[i][0]
			self.posColorNormalBuffer[i][1] = self.positionVbo[i][1]
			self.posColorNormalBuffer[i][2] = self.positionVbo[i][2]
			self.posColorNormalBuffer[i][3] = self.material.Kd[0]
			self.posColorNormalBuffer[i][4] = self.material.Kd[1]
			self.posColorNormalBuffer[i][5] = self.material.Kd[2]
			self.posColorNormalBuffer[i][6] = self.normalVbo[i][0]
			self.posColorNormalBuffer[i][7] = self.normalVbo[i][1]
			self.posColorNormalBuffer[i][8] = self.normalVbo[i][2]
			
	def buildPosColorTextureBuffer(self) :
		self.posColorTextureBuffer = numpy.empty([self.positionVbo.shape[0], 9], dtype=numpy.float32)
		for i in xrange(self.positionVbo.shape[0]) :
			self.posColorTextureBuffer[i][0] = self.positionVbo[i][0]
			self.posColorTextureBuffer[i][1] = self.positionVbo[i][1]
			self.posColorTextureBuffer[i][2] = self.positionVbo[i][2]
			self.posColorTextureBuffer[i][3] = self.material.Kd[0]
			self.posColorTextureBuffer[i][4] = self.material.Kd[1]
			self.posColorTextureBuffer[i][5] = self.material.Kd[2]
			self.posColorTextureBuffer[i][6] = self.textureVbo[i][0]
			self.posColorTextureBuffer[i][7] = self.textureVbo[i][1]
			self.posColorTextureBuffer[i][8] = 0
			
	def buildPosColorTextureNormalBuffer(self) :
		# print self.material.mapKd
		self.posColorTextureNormalBuffer = numpy.empty([self.positionVbo.shape[0], 12], dtype=numpy.float32)
		for i in xrange(self.positionVbo.shape[0]) :
			self.posColorTextureNormalBuffer[i][0] = self.positionVbo[i][0]
			self.posColorTextureNormalBuffer[i][1] = self.positionVbo[i][1]
			self.posColorTextureNormalBuffer[i][2] = self.positionVbo[i][2]
			self.posColorTextureNormalBuffer[i][3] = self.material.Kd[0]
			self.posColorTextureNormalBuffer[i][4] = self.material.Kd[1]
			self.posColorTextureNormalBuffer[i][5] = self.material.Kd[2]
			self.posColorTextureNormalBuffer[i][6] = self.textureVbo[i][0]
			self.posColorTextureNormalBuffer[i][7] = self.textureVbo[i][1]
			self.posColorTextureNormalBuffer[i][8] = 0
			self.posColorTextureNormalBuffer[i][9] = self.normalVbo[i][0]
			self.posColorTextureNormalBuffer[i][10] = self.normalVbo[i][1]
			self.posColorTextureNormalBuffer[i][11] = self.normalVbo[i][2]
		

class ObjLoader:
	def __init__(self) :
		pass
 
	def load(self, file):
		vboList = []
		positions = []
		normals = []
		textures = []
		faces = []
		materials = {}
		usemtl = None
		vbo = None
		with open(file) as f:
			for line in f:
				n = line.find('#')
				line = line[:n].strip().split()
				if line:
					if line[0] == 'mtllib' :
						materials = dict(materials.items() + self.loadMtl(line[1]).items())
					elif line[0] == 'usemtl' :
						if usemtl != None :
							if usemtl not in materials :
								print 'Error: mtl not define, vbo deleted'
							else :
								vbo = self.buildVBO(positions, textures, normals, faces, materials[usemtl])
						else :
							vbo = self.buildVBO(positions, textures, normals, faces, None)
						if vbo != None :
							vboList.append(vbo)
						faces = []
						vbo = None
						usemtl = line[1]
					elif line[0] == 'v':
						positions += [map(float, line[1:4])]
					elif line[0] == 'vn':
						normals += [map(float, line[1:4])]
					elif line[0] == 'vt':
						textures += [map(float, line[1:3])]
					elif line and line[0] == 'f':
						faces += self.parseFace(line[1:])
		
		# for key, mat in materials.items() :
			# mat.matPrint()
		
		if usemtl != None :
			if usemtl not in materials :
				print 'Error: mtl not define, vbo deleted'
			else :
				vbo = self.buildVBO(positions, textures, normals, faces, materials[usemtl])
		else :
			vbo = self.buildVBO(positions, textures, normals, faces, None)
		if vbo != None :
			vboList.append(vbo)
		return OBJ(vboList)
	
	def loadMtl(self, file) :
		materials = {}
		name = Ns = Ka = Kd = Ks = Ni = d = illum = mapKa = mapKd = mapKs = mapNs = mapd = None
		with open(file) as f:
			for line in f:
				n = line.find('#')
				line = line[:n].strip().split()
				if line :
					# print line
					if line[0] == 'newmtl' :
						if len(line) != 2 :
							print 'Error: bad mtl name, all mtl file ignored'
							return {}
						if name != None :
							if name in materials :
								print 'Error: this mtl already exist, old erased'
							materials[name] = Material(name, Ns, Ka, Kd, Ks, Ni, d, illum, mapKa, mapKd, mapKs, mapNs, mapd)
							name = Ns = Ka = Kd = Ks = Ni = d = illum = mapKa = mapKd = mapKs = mapNs = mapd = None
						name = line[1]
					elif line[0] == 'Ns' :
						if len(line) != 2 :
							print 'Error: Bad Ns, Ignored'
						else :
							Ns = line[1]
					elif line[0] == 'Ka' :
						if len(line) != 4 :
							print 'Error: Bad Ka, Ignored'
						else :
							Ka = [line[1], line[2], line[3]]
					elif line[0] == 'Kd' :
						if len(line) != 4 :
							print 'Error: Bad Kd, Ignored'
						else :
							Kd = [line[1], line[2], line[3]]
					elif line[0] == 'Ks' :
						if len(line) != 4 :
							print 'Error: Bad Ks, Ignored'
						else :
							Ks = [line[1], line[2], line[3]]
					elif line[0] == 'Ni' :
						if len(line) != 2 :
							print 'Error: Bad Ni, Ignored'
						else :
							Ni = line[1]
					elif line[0] == 'd' :
						if len(line) != 2 :
							print 'Error: Bad d, Ignored'
						else :
							d = line[1]
					elif line[0] == 'illum' :
						if len(line) != 2 :
							print 'Error: Bad illum, Ignored'
						else :
							illum = line[1]
					elif line[0] == 'map_Ka' :
						if len(line) != 2 :
							print 'Error: Bad map_Ka, Ignored'
						else :
							mapKa = line[1]
					elif line[0] == 'map_Kd' :
						if len(line) != 2 :
							print 'Error: Bad map_Kd, Ignored'
						else :
							mapKd = line[1]
					elif line[0] == 'map_Ks' :
						if len(line) != 2 :
							print 'Error: Bad map_Ks, Ignored'
						else :
							mapKs = line[1]
					elif line[0] == 'map_Ns' :
						if len(line) != 2 :
							print 'Error: Bad map_Ns, Ignored'
						else :
							mapNs = line[1]
					elif line[0] == 'map_d' :
						if len(line) != 2 :
							print 'Error: Bad map_d, Ignored'
						else :
							mapd = line[1]
					
						
		if name == None :
			print 'Eror: No mtl Name'
			return {}
		if name in materials :
			print 'Error: this mtl already exist, old erased'
		materials[name] = Material(name, Ns, Ka, Kd, Ks, Ni, d, illum, mapKa, mapKd, mapKs, mapNs, mapd)
		return materials
		
	
	def buildVBO(self, positions, textures, normals, faces, usemtl) :
		# print 'buildVBO'
		if len(faces) == 0:
			# print 'no usemtl'
			return None
		
		# print usemtl
		# print faces
		
		positionVbo = []
		textureVbo = []
		normalVbo = []
		tabs = [positions, textures, normals]
		tabsVbo = [positionVbo, textureVbo, normalVbo]
		
		lenPointDesc = len(faces[0])
		if lenPointDesc <= 0 :
			print 'Error: face have no description'
			return None
		if lenPointDesc > 3 :
			print 'Error: too much value for point description'
			return None
			
		if faces[0][0] == '' :
			print 'Error: no position value for point description'
			return None
		
		active = []
		for i in xrange(lenPointDesc) :
			if faces[0][i] != '' :
				active.append(True)
			else :
				active.append(False)
		
		for point in faces :
			if len(point) != lenPointDesc :
				print 'Error: all face have not the same lenght description'
				return None
			for i in xrange(lenPointDesc) :
				if point[i] == '' :
					tmpActive = False
				else :
					tmpActive = True
				if tmpActive != active[i] :
					print 'Error: all face have not the same description'
					return None
				# print point[i]
				if tmpActive :
					if int(point[i]) > len(tabs[i]) :
						print 'Error: face descriptor out for bound'
						# print i, point[i], len(tabs[i])
						return None
					tabsVbo[i].append(tabs[i][int(point[i]) - 1])
		
		
		positionVbo = numpy.array(tabsVbo[0], dtype=numpy.float32)
		textureVbo = numpy.array(tabsVbo[1], dtype=numpy.float32)
		normalVbo = numpy.array(tabsVbo[2], dtype=numpy.float32)
		# print 'positionVbo: ', positionVbo
		# print 'textureVbo: ', textureVbo
		# print 'normalVbo: ', normalVbo
		return  MyVBO(positionVbo, textureVbo, normalVbo, usemtl)
		
			
	
	def parseFace(self, face) :
		if len(face) == 4 :
			face = [face[0], face[1], face[3], face[1], face[2], face[3]]
		elif len(face) != 3 :
			print 'Error: bad number of point for this face'
			return []
		points = []
		for point in face :
			points.append(point.split('/'))
		return points
	
	def parse_face(self, vertex):
		# print vertex
		pattern = '(?P<v>\d*)/(?P<vt>\d*)/(?P<vn>\d*)'
		r = re.match(pattern, vertex)
		
		v = r.group('v')
		vt = r.group('vt')
		vn = r.group('vn')
		if not v :
			raise ValueError, "obj file bad formatted: need vertices"
		if not vn :
			raise ValueError, "obj file bad formatted: need normals"
		if not vt :
			vt = 1

		# return map(lambda x: int(x) - 1, [v, vt, vn])
		# print [v, vt, vn]
		return [v, vt, vn]