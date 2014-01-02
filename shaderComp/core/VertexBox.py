from Box import *

class VertexBox(Box):

	def __init__(self, name, linkManager, shaderType):
		Box.__init__(self, name, linkManager, shaderType)
		
	def getShaderType(self) :
		return 0
		