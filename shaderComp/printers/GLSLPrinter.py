##
# \authors Romain GUYOT de la HARDROUYERE
# \authors Matthieu BOURNAT
# \authors Antoine CHESNEAU
# \package shaderComp.printers
# \brief The GLSLPrinter is use to compute the GLSL Code of a project
# \version 0.1
# \date 2013-01-10

__name__ = "shaderComp.printers.GLSLPrinter"
__package__ = "shaderComp.printers"

from ..core.Printer import *
from ..core.Render import *
import os


class Printers(Printer):

	def __init__(self, projName, vertexNodeList, pixelNodeList):
		Printer.__init__(self, projName, vertexNodeList, pixelNodeList)
		self.name = 'GLSLPrinter'


	def compute(self, project) :
		print 'GLSL Printer Compute: ', self.projName
		self.applyCompute(self.vertexNodeList + self.pixelNodeList)
		self.applyDeclaration()
		self.finishCompute()

	def render(self) :
		print 'GLSL Printer Render: ', self.projName
		self.applyCompute(self.vertexNodeList + self.pixelNodeList)
		self.applyDeclaration()
		self.finishRender()

	def applyCompute(self, nodeList) :
		for node in nodeList :
			# if project
			if node.getType() == 0 :
				self.applyCompute(node.getNodeList())
			#if shader
			else:
				# if vextex shader
				if node.getShaderType() == 0 :
					if self.vertexShaderBuffer == '' :
						self.vertexShaderBuffer = self.writeHead(self.vertexShaderBuffer)
					try:
						name = node.__class__.__name__ + self.name
						# importation dynamique des printers
						mod = imp.load_source(name, 'shaderComp/printers/' + node.__class__.__module__.replace('shaderComp.shaders.', '').replace('.', '/')  + '/' + name + '.py')
						obj = mod.Gen(node.getParams())
						tmp = obj.compute(self)
						self.vertexShaderBuffer = self.vertexShaderBuffer + tmp + '\n'
					except IOError:
						print "fichier manquant: " + name

				# if fragment shader
				else :
					if self.fragmentShaderBuffer == '' :
						self.fragmentShaderBuffer = self.writeHead(self.fragmentShaderBuffer)
					try:
						name = node.__class__.__name__ + self.name
						# importation dynamique des printers
						mod = imp.load_source(name, 'shaderComp/printers/' + node.__class__.__module__.replace('shaderComp.shaders.', '').replace('.', '/') + '/' + name + '.py')
						obj = mod.Gen(node.getParams())
						tmp = obj.compute(self)
						self.fragmentShaderBuffer = self.fragmentShaderBuffer + tmp + '\n'
					except IOError:
						print "fichier manquant: " + name


	def writeHead(self, buffer) :
		buffer = buffer + 'void main(void) {\n'
		return buffer

	def applyDeclaration(self) :
		for name, declaration in self.vertexDeclaration.items() :
			if declaration[0] == None :
				self.vertexShaderBuffer = declaration[1] + ' '  + name + ';' + '\n' + self.vertexShaderBuffer
			else :
				self.vertexShaderBuffer = declaration[0] + ' '  + declaration[1] + ' '  + name + ';' + '\n' + self.vertexShaderBuffer
		for name, declaration in self.fragmentDeclaration.items() :
			if declaration[0] == None :
				self.fragmentShaderBuffer = declaration[1] + ' '  + name + ';' + '\n' + self.fragmentShaderBuffer
			else :
				self.fragmentShaderBuffer = declaration[0] + ' '  + declaration[1] + ' '  + name + ';' + '\n' + self.fragmentShaderBuffer

	# def addDeclaration(self, shaderType, declaration) :
		# name = ' dec' + str(self.nbDec) + '_' + str(int(time.time()))
		# self.nbDec += 1
		# if shaderType == 0 :
			# if self.vertexDeclaration.count(name) == 0 :
				# self.vertexShaderBuffer = declaration + name + ';' + '\n' + self.vertexShaderBuffer
				# self.vertexDeclaration.append(name)
		# elif shaderType == 1 :
			# if self.fragmentDeclaration.count(name) == 0 :
				# self.fragmentShaderBuffer = declaration + name + ';' + '\n' + self.fragmentShaderBuffer
				# self.fragmentDeclaration.append(name)
		# return name

	# def addDeclaration(self, shaderType, declaration, name) :
		# if shaderType == 0 :
			# self.vertexShaderBuffer = declaration + ' ' + name + ';' + '\n' + self.vertexShaderBuffer
		# elif shaderType == 1 :
			# self.fragmentShaderBuffer = declaration + ' ' + name + ';' + '\n' + self.fragmentShaderBuffer
		# return name

	def finishCompute(self) :
		if not os.path.exists(self.projName):
			os.makedirs(self.projName)
		if self.vertexShaderBuffer != '' :
			self.vertexShaderBuffer = self.vertexShaderBuffer + '}\n'
			file = open(self.projName + '/vertexShader.glsl', 'w')
			file.write(self.vertexShaderBuffer)
			file.close()
		if self.fragmentShaderBuffer != '' :
			self.fragmentShaderBuffer = self.fragmentShaderBuffer + '}\n'
			file = open(self.projName + '/fragmentShader.glsl', 'w')
			file.write(self.fragmentShaderBuffer)
			file.close()

	def finishRender(self) :
		if self.vertexShaderBuffer != '' :
			self.vertexShaderBuffer = self.vertexShaderBuffer + '}\n'
		if self.fragmentShaderBuffer != '' :
			self.fragmentShaderBuffer = self.fragmentShaderBuffer + '}\n'

		progs = []
		progs.append(self.vertexShaderBuffer)
		progs.append(self.fragmentShaderBuffer)
		render = Render()
		render.execute(progs)

