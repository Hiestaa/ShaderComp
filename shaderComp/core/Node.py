from Var import *

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.core.Node
# @brief This class represent the parent class of all nodes
# @version 1.0
# @date 2014-01-13
# @details It can be a shader as well as a box. It can be a pixel-node or a vertex-node.

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class Node
# @brief This class represent the parent class of all nodes
# @version 1.0
# @date 2014-01-13
# @details It can be a shader as well as a box. It can be a pixel-node or a vertex-node.


class Node:

	def __init__(self, type, shaderType):
		self.type = type
		self.name = 'None'
		self.linkList = []
		self.linkManager = None
		self.shaderType = shaderType
		self.inVars = {}
		self.outVars = {}

	def getName(self) :
		return self.name

	def setName(self, name) :
		self.name = name

	def getType(self) :
		return self.type

	def getShaderType(self) :
		return self.shaderType

	def setLinkManager(self, linkManager) :
		self.linkManager = linkManager

	def getLinkList(self) :
		return self.linkList

	def setLinkList(self, value) :
		self.linkList = value

	## @fn getInVar(name)
	# @brief Retrieve an input variable of the node using its name
	# @param name A string giving the name of the variable
	# @return A reference on the corresponding variable
	def getInVar(self, name) :
		return self.inVars[name]

	## @fn getOutVar(name)
	# @brief Retrieve an output variable of the node using its name
	# @param name A string giving the name of the variable
	# @return A reference on the corresponding variable
	def getOutVar(self, name) :
		return self.outVars[name]

	def getInVarList(self) :
		return self.inVars

	def getOutVarList(self) :
		return self.outVars
