from Box import *

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.core.VertexBox
# @brief This class is a Box of vertex nodes
# @version 1.0
# @date 2014-01-07
# @details A vertexBox is automatically created for each project. It handles all the nodes of type Vertex

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class VertexBox
# @brief This class is a Box of vertex nodes
# @version 1.0
# @date 2014-01-07
# @details A vertexBox is automatically created for each project. It handles all the nodes of type Vertex

class VertexBox(Box):

	def __init__(self, name, linkManager, shaderType):
		Box.__init__(self, name, linkManager, shaderType)

	def getShaderType(self) :
		return 0
