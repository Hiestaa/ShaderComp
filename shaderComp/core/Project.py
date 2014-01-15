from VertexBox import *
from PixelBox import *
from LinkManager import *
import imp

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class Project
# @brief This class is the main entry point of the library
# @version 0.1
# @date 2013-11-07
# @details Instanciation of a Project object will give an access to
# all the core features of the library, like adding nodes and variables and creating links between the variables

class Project():
	## @fn __init__(name)
	# @brief Instanciate an new project
	# @param name Gve a name to this project
	def __init__(self, name) :
		self.name = name
		self.linkManager = LinkManager(self)
		self.vertexBox = VertexBox('Vertex' + self.name, self.linkManager, 0)
		self.pixelBox = PixelBox('Pixel' + self.name, self.linkManager, 1)

	## @fn getVertexBox()
	# @brief Give an access to the VertexBox specific features
	# @details The VertexBox is the box wich stores the nodes of type _vertex shader_.
	# @return The VertexBox used in this project
	# @see class shaderComp.core.Box, class shaderComp.core.VertexBox
	def getVertexBox(self) :
		return self.vertexBox

	## @fn getPixelBox()
	# @brief Give an access to the PixelBox specific features
	# @details The PixelBox is the box wich stores the nodes of type _vertex shader_.
	# @return The PixelBox used in this project
	# @see class shaderComp.core.Box, class shaderComp.core.PixelBox
	def getPixelBox(self) :
		return self.pixelBox

	## @fn getBox(box)
	# @brief give an access to one of the box of the project
	# @details This is not advised to use this function as it uses a string comparison.
	# Prefer using the getVertexBox or the getPixelBox function
	# @param box A string specifying which box the box to get. Supported values are:
	# - `"Vertex|vertex"`: get the vertex box
	# - `"Pixel|pixel"`: get the pixel box
	# @return The box needed
	# @see class shaderComp.core.Box, class shaderComp.core.PixelBox
	# @see functions getVertexBox(), getPixelBox()
	def getBox(self, box) :
		if box == 'Vertex' or box == 'vertex' :
			return self.vertexBox
		elif box == 'Pixel' or box == 'pixel' :
			return self.pixelBox
		else :
			print 'Error: Box No Exist'

	## @fn getLinkList(box)
	# @brief Give an access to the list of links of the specified box
	# @param box A string specifying in wich box to get the list of links. Supported values are:
	# - `"Vertex|vertex"`: get the links of the pixel box
	# - `"Pixel|pixel"`: get the links of the vertex box
	# @return A list of links stored in the specified box
	# @see class shaderComp.core.Link
	def getLinkList(self, box) :
		if box == 'Vertex' or box == 'vertex' :
			return self.vertexBox.getLinkList()
		elif box == 'Pixel' or box == 'pixel' :
			return self.pixelBox.getLinkList()
		else :
			print 'Error: Box No Exist'

	## @fn clearBox(box)
	# @brief Clear the box by deleting all the node it contains
	# @param box a string specifying wich box to clear. Supported values are:
	# - `"Vertex|vertex"`: All the nodes of the vertex box will be deleted
	# - `"Pixel|pixel"`: All the nodes of the pixel box will be deleted
	# - `"All|all"`: all the boxes will be cleared
	def clearBox(self, box) :
		if box == 'Vertex' or box == 'vertex' :
			self.vertexBox.clear()
		elif box == 'Pixel' or box == 'pixel' :
			self.pixelBox.clear()
		elif box == 'All' or box == 'all' :
			self.vertexBox.clear()
			self.pixelBox.clear()
		else :
			print 'Error: Box No Exist'

	## @fn clear()
	# @brief Delete all the nodes of this project (both boxes)
	def clear(self) :
		self.vertexBox.clear()
		self.pixelBox.clear()

	## @fn addNode(node, pos)
	# @brief Add a new node to this project at the given position
	# @details The node will be added in the right box according to the type of the shader it represents
	# @param node A reference to an object of type `Node` or any of its children. This could be a Box as well as a Shader child.
	# @param pos The position where to add this node. Be careful that the position is relative to the box in which the shader will be added.
	def addNode(self, node, pos) :
		if node.getShaderType() == 0 :
			self.vertexBox.addNode(node, pos)
		elif node.getShaderType() == 1 :
			self.pixelBox.addNode(node, pos)

	## @fn appendNode(node)
	# @brief Add a new node to this project at the end of the right box
	# @details The node will be appended to the list of nodes in the right box according to the type of the shader it represents
	# @param node A reference to an object of type `Node` or any of its children. This could be a Box as well as a Shader child.
	def appendNode(self, node) :
		if node.getShaderType() == 0 :
			self.vertexBox.appendNode(node)
		elif node.getShaderType() == 1 :
			self.pixelBox.appendNode(node)

	## @fn removeNode(node)
	# @brief Remove the given node from the project
	# @details The node will be removed from the list of nodes in the right box according to the type of the shader it represents
	# @param node A reference to an object of type `Node` or any of its children. This could be a Box as well as a Shader child.
	def removeNode(self, node) :
		if node.getShaderType() == 0 :
			self.vertexBox.removeNode(node)
		elif node.getShaderType() == 1 :
			self.pixelBox.removeNode(node)

	## @fn removeNodeAt(pos, box)
	# @brief Remove the node at the given position from the given box
	# @details The node will be removed from the list of nodes in the specified box
	# @param pos An integer representing the position of the node to remove. Be careful that the position is relative to the box storing the list.
	# @param Box A string specifying the box. Supported values are:
	# - `"Vertex|vertex"`: All the node at the given position in the vertex box will be removed
	# - `"Pixel|pixel"`: All the nodes at the given position in the pixel box will be removed
	def removeNodeAt(self, pos, box) :
		if box == 'Vertex' or box == 'vertex' :
			self.vertexBox.removeNodeAt(pos)
		elif box == 'Pixel' or box == 'pixel' :
			self.pixelBox.removeNodeAt(pos)
		else :
			print 'Error: Box No Exist'

	## @fn addVertexInVar(name, type)
	# @brief Create a new input variable for the vertex box
	# @details Adding an input variable to a box allows to link this variable to the input variable of one of the node that the box contains
	# The links between nodes will then be used for the generation of random unique variables names in the shader, avoind conflict between nodes.
	# @param name A string representing the name of the variable, will be used to retrieve the variable if the reference returned is lost.
	# Note that the namepaces are local to a node, so there cannot be any conflict between two node with the same input variable name.
	# There can even not be any conflict between the input variable names and the output variable names of the same node.
	# @param type A string specifying the type of the variable. Supported valued are all the GLSL commonly used variable types.
	# @return A reference on the created variable.
	# @see shaderComp.core.Var
	def addVertexInVar(self, name, type) :
		return self.vertexBox.addInVar(name, type)

	## @fn addVertexOutVar(name, type)
	# @brief Create a new output variable for the vertex box
	# @details Adding an output variable to a box allows to link this variable to the output variable of one of the node that the box contains
	# The links between nodes will then be used for the generation of random unique variables names in the shader, avoind conflict between nodes.
	# @param name A string representing the name of the variable, will be used to retrieve the variable if the reference returned is lost.
	# Note that the namepaces are local to a node, so there cannot be any conflict between two node with the same output variable name.
	# There can even not be any conflict between the output variable names and the output variable names of the same node.
	# @param type A string specifying the type of the variable. Supported valued are all the GLSL commonly used variable types.
	# @return A reference on the created variable.
	# @see shaderComp.core.Var
	def addVertexOutVar(self, name, type) :
		return self.vertexBox.addOutVar(name, type)

	## @fn addVertexUniform(name, value, type)
	# @brief Create a new uniform variable for the vertex box
	# @details Adding a uniform to a box can be needed to allow dynamic configuration of the resulting shader from the program that will execute it.
	# @param name A string representing the name of the variable, will be used to retrieve the variable if the reference returned is lost.
	# Note that the uniform created will be available in all the shaders of the box
	# @param value The real name to give to this uniform as it will be written in the generated file
	# @param type A string specifying the type of the variable. Supported valued are all the GLSL commonly used variable types.
	# @return A reference on the created variable.
	# @see shaderComp.core.Var
	def addVertexUniform(self, name, value, type) :
		return self.vertexBox.addUniform(name, value, type)

	## @fn addPixelInVar(name, type)
	# @brief Create a new output variable for the pixel box
	# @details Adding an output variable to a box allows to link this variable to the output variable of one of the node that the box contains
	# The links between nodes will then be used for the generation of random unique variables names in the shader, avoind conflict between nodes.
	# @param name A string representing the name of the variable, will be used to retrieve the variable if the reference returned is lost.
	# Note that the namepaces are local to a node, so there cannot be any conflict between two node with the same output variable name.
	# There can even not be any conflict between the output variable names and the output variable names of the same node.
	# @param type A string specifying the type of the variable. Supported valued are all the GLSL commonly used variable types.
	# @return A reference on the created variable.
	# @see shaderComp.core.Var
	def addPixelInVar(self, name, type) :
		return self.pixelBox.addInVar(name, type)

	## @fn addPixelOutVar(name, type)
	# @brief Create a new output variable for the pixel box
	# @details Adding an output variable to a box allows to link this variable to the output variable of one of the node that the box contains
	# The links between nodes will then be used for the generation of random unique variables names in the shader, avoind conflict between nodes.
	# @param name A string representing the name of the variable, will be used to retrieve the variable if the reference returned is lost.
	# Note that the namepaces are local to a node, so there cannot be any conflict between two node with the same output variable name.
	# There can even not be any conflict between the output variable names and the output variable names of the same node.
	# @param type A string specifying the type of the variable. Supported valued are all the GLSL commonly used variable types.
	# @return A reference on the created variable.
	# @see shaderComp.core.Var
	def addPixelOutVar(self, name, type) :
		return self.pixelBox.addOutVar(name, type)

	## @fn addPixelUniform(name, value, type)
	# @brief Create a new uniform variable for the pixel box
	# @details Adding a uniform to a box can be needed to allow dynamic configuration of the resulting shader from the program that will execute it.
	# @param name A string representing the name of the variable, will be used to retrieve the variable if the reference returned is lost.
	# Note that the uniform created will be available in all the shaders of the box
	# @param value The real name to give to this uniform as it will be written in the generated file
	# @param type A string specifying the type of the variable. Supported valued are all the GLSL commonly used variable types.
	# @return A reference on the created variable.
	# @see shaderComp.core.Var
	def addPixelUniform(self, name, value, type) :
		return self.pixelBox.addUniform(name, value, type)

	## @fn getVertexInVar(name)
	# @brief Retrieve an input variable of the vertex box using its name
	# @param name A string giving the name of the variable
	# @return A reference on the corresponding variable
	def getVertexInVar(self, name) :
		return self.vertexBox.getInVar(name)

	## @fn getVertexOutVar(name)
	# @brief Retrieve an output variable of the vertex box using its name
	# @details nothing
	# @param name A string giving the name of the variable
	# @return A reference on the corresponding variable
	def getVertexOutVar(self, name) :
		return self.vertexBox.getOutVar(name)

	## @fn getVertexUniform(name)
	# @brief Retrieve a uniform variable of the vertex box using its name
	# @param name A string giving the name of the variable
	# @return A reference on the corresponding variable
	def getVertexUniform(self, name) :
		return self.vertexBox.getUniform(name)

	## @fn getVertexPipelineVar(name)
	# @brief Retrieve a pipeline variable of the vertex box using its name
	# @param name A string giving the name of the variable
	# @return A reference on the corresponding variable
	def getVertexPipelineVar(self, name) :
		return self.vertexBox.getPipelineVar(name)

	## @fn getPixelInVar(name)
	# @brief Retrieve an input variable of the pixel box using its name
	# @param name A string giving the name of the variable
	# @return A reference on the corresponding variable
	def getPixelInVar(self, name) :
		return self.pixelBox.getInVar(name)

	## @fn getPixelOutVar(name)
	# @brief Retrieve an output variable of the pixel box using its name
	# @param name A string giving the name of the variable
	# @return A reference on the corresponding variable
	def getPixelOutVar(self, name) :
		return self.pixelBox.getOutVar(name)

	## @fn getPixelUniform(name)
	# @brief Retrieve a uniform variable of the pixel box using its name
	# @param name A string giving the name of the variable
	# @return A reference on the corresponding variable
	def getPixelUniform(self, name) :
		return self.pixelBox.getUniform(name)

	## @fn getPixelPipelineVar(name)
	# @brief Retrieve a pipeline variable of the pixel box using its name
	# @param name A string giving the name of the variable
	# @return A reference on the corresponding variable
	def getPixelPipelineVar(self, name) :
		return self.pixelBox.getPipelineVar(name)

	## @fn addLinkNode(nodeFrom, varFrom, nodeTo, varTo)
	# @brief Create a link between two variables
	# @details Creating a link between two variables of two node will result in the copying the resulting value of the varFrom output
	# to the varTo input.
	# It is possible to create multiple links going from the same output variable: the value will be copied in each of the destinations of the link.
	# However, it is not possible to create multiple links going to the same input variable as this input cannot take more than one value, this could bring unexpected results.
	# @param nodeFrom A reference on the node where to find the output variable that will be linked
	# @param nodeTo A reference on the node where to find the input variable that will be linked to this output
	# @param varFrom A reference on the output variable where the link comes from
	# @param varTo A reference on the output variable where the link goes to
	def addLinkNode(self, nodeFrom, varFrom, nodeTo, varTo) :
		self.linkManager.addLinkNode(nodeFrom, varFrom, nodeTo, varTo)

	## @fn addLink(varFrom, varTo)
	# @brief Create a link between two variables
	# @details Creating a link between two variables will result in the copying the resulting value of the varFrom output
	# to the varTo input.
	# It is possible to create multiple links going from the same output variable: the value will be copied in each of the destinations of the link.
	# However, it is not possible to create multiple links going to the same input variable as this input cannot take more than one value, this could bring unexpected results.
	# @param varFrom A reference on the output variable where the link comes from
	# @param varTo A reference on the output variable where the link goes to
	def addLink(self, varFrom, varTo) :
		self.linkManager.addLink(varFrom, varTo)

	## @fn addValuedLinkNode(nodeTo, varTo, value)
	# @brief Create a link between a constant (a value) and an input variable
	# @details Creating a valuedLink allows to set an input variable as a constant, giving the value of the constant.
	# The same restriction applies on the variable destination of the link: it cannot be uses multiplie times, as a variable cannot have multiple values.
	# @param nodeTo A reference on the node where to find the input variable that will be set to the given value
	# @param varTo A reference on the output variable where the link goes to
	# @param value The value to set
	def addValuedLinkNode(self, nodeTo, varTo, value) :
		self.linkManager.addValuedLinkNode(nodeTo, varTo, value)

	## @fn addValuedLink(varTo, value)
	# @brief Create a link between a constant (a value) and an input variable
	# @details Creating a valuedLink allows to set an input variable as a constant, giving the value of the constant.
	# The same restriction applies on the variable destination of the link: it cannot be uses multiplie times, as a variable cannot have multiple values.
	# @param varTo A reference on the output variable where the link goes to
	# @param value The value to set
	def addValuedLink(self, varTo, value) :
		self.linkManager.addValuedLink(varTo, value)

	## @fn addValuedLinkByName(nodeTo, nameVarTo, value)
	# @brief Create a link between a constant (a value) and an input variable
	# @details Creating a valuedLink allows to set an input variable as a constant, giving the value of the constant.
	# The same restriction applies on the variable destination of the link: it cannot be uses multiplie times, as a variable cannot have multiple values.
	# @param nodeTo A reference on the node where to find the input variable that will be set to the given value
	# @param nameVarTo The name of a reference on the output variable where the link goes to
	# @param value The value to set
	def addValuedLinkByName(self, nodeTo, nameVarTo, value) :
		self.linkManager.addValuedLinkByName(nodeTo, nameVarTo, value)

	## @fn deleteLink(link)
	# @brief Delete a link using its reference
	# @param link A reference on the link to delete
	def deleteLink(self, link) :
		self.linkManager.deleteLink(link)

	## @fn deleteLink(nodeFrom, nodeTo, varFrom, varTo)
	# @brief Delete a link between two variables of two nodes
	# @param nodeFrom A reference on the node where to find the output variable that is linked
	# @param nodeTo A reference on the node where to find the input variable that is to this output
	# @param varFrom A reference on the output variable where the link comes from
	# @param varTo A reference on the output variable where the link goes to
	def deleteLink(self, nodeFrom, nodeTo, varFrom, varTo) :
		self.linkManager.deleteLink(nodeFrom, nodeTo, varFrom, varTo)

	## @fn deleteValuedLink(nodeTo, varTo)
	# @brief Delete a link between a constant and a variable
	# @param nodeTo A reference on the node where to find the input variable
	# @param varTo A reference on the output variable where the link goes to
	def deleteValuedLink(self, nodeTo, varTo) :
		self.linkManager.deleteValuedLink(nodeTo, varTo)

	## @fn compute(printerName)
	# @brief Compute the generation of the source code of the vertex shader and the pixel shader.
	# @details Before the generation of the source code, the links are used to set the name of the variable randomly,
	# with the insurance that two different variables will have two different names
	# The source code will be generated in two distinct file which name is generated as described below:
	# 1. `fragmentShader[ProjName].[ext]`: will contain the surce code of the fragment shader. The [ProjName] is the
	#	name of the project specified when creating it, the [ext] depends on the printer used for the generation.
	# 2. `fragmentShader[ProjName].[ext]`: will contain the surce code of the vertex shader. The [ProjName] is the
	#	name of the project specified when creating it, the [ext] depends on the printer used for the generation.
	# @param printerName A string used to know wich printer to use. Up now, supported values are:
	# - `"GLSLPrinter"`: Generate the source code for an OpenGL program using GLSL. Extension of the generated files will be `.glsl`.
	def compute(self, printerName) :
		try:
			import shaderComp.printers
			mod = imp.load_source(printerName, 'shaderComp/printers/' +printerName + '.py')
			printer = mod.Printers(self.name, self.vertexBox.getNodeList(), self.pixelBox.getNodeList())

		except IOError:
			print "Error: Printer " + printerName + " Not Found ",
		try:
			printer.applyVarNameSelection(self)
			printer.compute(self)
			printer.removeAllVarName(self)
		except IOError as e:
			print "Error: ", e

	## @fn render()
	# @brief Display an overview of the result of the shader built in this project.
	# @details This will generate a GLSL version of the shader, compile it and display it in
	#  a window with some models spinning with the use of the library OpenGL.
	def render(self) :
		printerName = 'GLSLPrinter'
		try:
			mod = imp.load_source(printerName, 'shaderComp/printers/' +printerName + '.py')
			printer = mod.Printers(self.name, self.vertexBox.getNodeList(), self.pixelBox.getNodeList())
		except IOError:
			print "Error: Printer " + printerName + " Not Found "
		try:
			printer.applyVarNameSelection(self)
			printer.render()
			printer.removeAllVarName(self)
		except IOError as e:
			print "Error: ", e

	## @fn save(name)
	# @brief Save the project to the given file
	# @param name A string specifying the name of the file to which to save the project.
	def save(self, name) :
		outfile = open(name, "wb")
		pickle.dump(self, outfile)
		outfile.close()

	## @fn load(name)
	# @brief Load the project from the given file
	# @param name A string specifying the name of the file in which the project has been previously saved.
	# @return A reference on a fresh instance of the class project which is the exact copy of the previously saved one.
	@staticmethod
	def load(name) :
		infile = open(name, "rb")
		tmp = pickle.load(infile)
		return tmp

	## @fn saveBox(name, box)
	# @brief Save the content of one of the box in the given file
	# @param name A string specifying the name of the file in which to save the box
	# @param box A string specifying which box to save. Supported values are:
	# - `"Vertex|vertex"`: save the vertex box
	# - `"Pixel|pixel"`: save the pixel box
	def saveBox(self, name, box) :
		if box == 'Vertex' or box == 'vertex' :
			tmpList = self.linkManager.popOneBoxLinkBetwinBox(self.vertexBox, self.pixelBox)
			self.vertexBox.save(name)
			self.linkManager.addLinkListOnBox(self.vertexBox, tmpList)
		elif box == 'Pixel' or box == 'pixel' :
			tmpList = self.linkManager.popOneBoxLinkBetwinBox(self.pixelBox, self.vertexBox)
			self.pixelBox.save(name)
			self.linkManager.addLinkListOnBox(self.pixelBox, tmpList)
		else :
			print 'Error: Box No Exist'

	## @fn loadBox(name, box)
	# @brief Load the content of one of the box from the given file
	# @param name A string specifying the name of the file in which the box has been previously saved
	# @param box A string specifying which box to load. Supported values are
	# - `"Vertex|vertex"`: load the vertex box
	# - `"Pixel|pixel"`: load the pixel box
	def loadBox(self, name, box) :
		if box == 'Vertex' or box == 'vertex' :
			self.linkManager.deleteAllLinkBetwinBox()
			self.vertexBox = self.vertexBox.load(name)
		elif box == 'Pixel' or box == 'pixel' :
			self.linkManager.deleteAllLinkBetwinBox()
			self.pixelBox = self.pixelBox.load(name)
		else :
			print 'Error: Box No Exist'

	## @fn loadBoxAsNode(name, box)
	# @brief Load the content of one of the box from the given file
	# @param name A string specifying the name of the file in which the box has been previously saved
	# @return A reference on the loaded box.
	def loadBoxAsNode(self, name) :
		return self.vertexBox.load(name)

	## @fn printProjectListName()
	# @brief Print the list of nodes (using their names) added to each box of the project
	# @details This function can be used for debug purposes
	def printProjectListName(self) :
		print self.name
		self.printVertexNodeListName()
		self.printPixelNodeListName()

	## @fn printVertexNodeListName()
	# @brief Print the list of nodes (using their names) of type `vertex shader` added to the project
	# @details This function can be used for debug purposes
	def printVertexNodeListName(self) :
		self.vertexBox.printListName()

	## @fn printPixelNodeListName()
	# @brief Print the list of nodes (using their names) of type `pixel shader` added to the project
	# @details This function can be used for debug purposes
	def printPixelNodeListName(self) :
		self.pixelBox.printListName()