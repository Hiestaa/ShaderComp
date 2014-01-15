from Node import *

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.core.Shader
# @brief Subclass of Node
# @version 1.0
# @date 2014-01-13
# @details All shader plugins have to inherit from this class

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class Shader
# @brief Subclass of Node
# @version 1.0
# @date 2014-01-13
# @details All shader plugins have to inherit from this class
class Shader(Node):

	## @fn __init__(name, shaderType)
	# @brief Instanciate an new shader.
	# @param shaderType Int allowing us to know if it's a VertexShader or a PixelShader.
	def __init__(self, shaderType):
		Node.__init__(self, 1, shaderType)
		self.shaderType = shaderType

	def getParams(self) :
		return (self.inVars, self.outVars)

	def printName(self) :
		print self.name