from Box import *

class PixelBox(Box):

	def __init__(self, name, linkManager, shaderType):
		Box.__init__(self, name, linkManager, shaderType)
	
	def getShaderType(self) :
		return 1
		