from Node import *
from Pipeline import *
import pickle

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.core.Box
# @brief This class is a Box of nodes
# @version 1.0
# @date 2014-01-07
# @details Box objects will be instantiated for each project (a VertexBox and a PixelBox),
# this class provides a number of features for the handling of its nodes.

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class Box
# @brief This class is a Box of nodes
# @version 1.0
# @date 2014-01-07
# @details Box objects will be instantiated for each project (a VertexBox and a PixelBox),
# this class provides a number of features for the handling of its nodes.
class Box(Node):

	## @fn __init__(name, linkManager, shaderType)
	# @brief Instanciate an new box.
	# @param name Give a name to this box.
	# @param linkManager An instantiated LinkManager of the current project.
	# @param shaderType An int allowing us to know if it's a VertexBox or a PixelBox.
	def __init__(self, name, linkManager, shaderType) :
		Node.__init__(self, 0, shaderType)
		self.nodeList = []
		self.name = name
		self.linkList = []
		self.linkManager = linkManager
		self.uniforms = {}
		self.pipeline = Pipeline.getPipelineVars(self)

	## @fn getNodeList()
	# @brief Give an access to the list of nodes of the box.
	# @return A list of nodes stored in the box.
	def getNodeList(self) :
		return self.nodeList

	## @fn getUniforms()
	# @brief Give an access to the list of uniforms of the box.
	# @return A list of uniforms stored in the box.
	def getUniforms(self) :
		return self.uniforms

	## @fn clear()
	# @brief Clear the box by deleting all the node it contains.
	def clear(self) :
		self.nodeList = []

	## @fn addNode(node, pos)
	# @brief Add a new node to this box at the given position.
	# @details The node will be added in the box.
	# @param node A reference to an object of type `Node` or any of its children. This could be a Box as well as a Shader child.
	# @param pos The position where to add this node. Be careful that the position is relative to the box in which the shader will be added.
	def addNode(self, node, pos) :
		if node.getType() == 0 :
			self.linkList = self.linkList + node.getLinkList()
			#node.setLinkList([])
		node.setLinkManager(self.linkManager)
		self.nodeList.insert(pos, node)

	## @fn appendNode(node)
	# @brief Add a new node at the end of the list of nodes of this box.
	# @details The node will be appended to the list of nodes in the box.
	# @param node A reference to an object of type `Node` or any of its children. This could be a Box as well as a Shader child.
	def appendNode(self, node) :
		if node.getType() == 0 :
			self.linkList = self.linkList + node.getLinkList()
			#node.setLinkList([])
		node.setLinkManager(self.linkManager)
		self.nodeList.append(node)

	## @fn removeNode(node)
	# @brief Remove the given node.
	# @details The node will be removed from the list of nodes in the box.
	# @param node A reference to an object of type `Node` or any of its children. This could be a Box as well as a Shader child.
	def removeNode(self, node) :
		self.nodeList.pop(self.nodeList.index(node))

	## @fn removeNodeAt(pos)
	# @brief Remove the node at the given position from the box.
	# @details The node will be removed from the list of nodes in the box.
	# @param pos An integer representing the position of the node to remove. Be careful that the position is relative to the box storing the list.
	def removeNodeAt(self, pos) :
		self.nodeList.pop(pos)

	## @fn addInVar(name, type)
	# @brief Create a new input variable for the box.
	# @details Adding an input variable to a box allows to link this variable to the input variable of one of the node that the box contains
	# The links between nodes will then be used for the generation of random unique variables names in the shader, avoiding conflict between nodes.
	# @param name A string representing the name of the variable, will be used to retrieve the variable if the reference returned is lost.
	# Note that the namepaces are local to a node, so there cannot be any conflict between two node with the same input variable name.
	# There can even not be any conflict between the input variable names and the output variable names of the same node.
	# @param type A string specifying the type of the variable. Supported valued are all the GLSL commonly used variable types.
	# @return A reference on the created variable.
	# @see shaderComp.core.Var
	def addInVar(self, name, type) :
		self.inVars[name] = Var(name, self, VarType.IN, type)
		return self.inVars[name]

	## @fn addOutVar(name, type)
	# @brief Create a new output variable for the box.
	# @details Adding an output variable to a box allows to link this variable to the output variable of one of the node that the box contains
	# The links between nodes will then be used for the generation of random unique variable names in the shader, avoiding conflict between nodes.
	# @param name A string representing the name of the variable, will be used to retrieve the variable if the reference returned is lost.
	# Note that the namepaces are local to a node, so there cannot be any conflict between two node with the same output variable name.
	# There can even not be any conflict between the output variable names and the input variable names of the same node.
	# @param type A string specifying the type of the variable. Supported valued are all the GLSL commonly used variable types.
	# @return A reference on the created variable.
	# @see shaderComp.core.Var
	def addOutVar(self, name, type) :
		self.outVars[name] = Var(name, self, VarType.OUT, type)
		return self.outVars[name]

	## @fn addUniform(name, value, type)
	# @brief Create a new uniform variable for the box.
	# @details Adding a uniform to a box can be needed to allow dynamic configuration of the resulting shader from the program that will execute it.
	# @param name A string representing the name of the variable, will be used to retrieve the variable if the reference returned is lost.
	# Note that the uniform created will be available in all the shaders of the box.
	# @param value The value to give to this uniform.
	# @param type A string specifying the type of the variable. Supported valued are all the GLSL commonly used variable types.
	# @return A reference on the created variable.
	# @see shaderComp.core.Var
	def addUniform(self, name, value, type) :
		self.uniforms[name] = Var(name, self, VarType.UNI, type, value)
		return self.uniforms[name]

	## @fn getUniform(name)
	# @brief Retrieve a uniform variable of the box using its name.
	# @param name A string giving the name of the variable.
	# @return A reference on the corresponding variable.
	def getUniform(self, name) :
		return self.uniforms[name]

	## @fn getPipelineVar(name)
	# @brief Retrieve a pipeline variable of the box using its name.
	# @param name A string giving the name of the variable.
	# @return A reference on the corresponding variable.
	def getPipelineVar(self, name) :
		return self.pipeline[name]

	## @fn save(name)
	# @brief Save the content the box to the given file;
	# @param name A string specifying the name of the file to which to save the project.
	def save(self, name) :
		outfile = open(name, "wb")
		pickle.dump(self, outfile)
		outfile.close()

	## @fn load(name)
	# @brief Load the content of the box from the given file.
	# @param name A string specifying the name of the file in which the box has been previously saved.
	def load(self, name) :
		infile = open(name, "rb")
		tmp = pickle.load(infile)
		return tmp

	## @fn printListName()
	# @brief Print the list of nodes (using their names) of the box.
	# @details This function can be used for debug purposes
	def printListName(self) :
		print 'Box : ' + self.name + ', Nodes Name: '
		for node in self.nodeList :
			if node.getType() == 0 :
				node.printListName()
			else :
				node.printName()
