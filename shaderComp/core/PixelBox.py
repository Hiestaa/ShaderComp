from Box import *

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.core.PixelBox
# @brief This class is a Box of pixel nodes
# @version 1.0
# @date 2014-01-07
# @details A pixelBox is automatically created for each project. It handles all the nodes of type Pixel

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class PixelBox
# @brief This class is a Box of pixel nodes
# @version 1.0
# @date 2014-01-07
# @details A pixelBox is automatically created for each project. It handles all the nodes of type Pixel

class PixelBox(Box):

	def __init__(self, name, linkManager, shaderType):
		Box.__init__(self, name, linkManager, shaderType)

	def getShaderType(self) :
		return 1
