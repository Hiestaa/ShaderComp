from Link import *
from ValuedLink import *
from Var import *

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class LinkManager
# @brief This class handles the links of a project
# @version 0.1
# @date 2014-01-13
# @details Class used to manage the links between nodes in a project
class LinkManager :

	## @fn __init__(name, project)
	# @brief Instanciate an new LinkManager.
	# @param name Set a project to this LinkManager.
	def __init__(self, project):
		self.project = project

	## @fn addLink(varFrom, varTo)
	# @brief Create a link between two variables
	# @details Creating a link between two variables will result in the copying the resulting value of the varFrom output
	# to the varTo input.
	# It is possible to create multiple links going from the same output variable: the value will be copied in each of the destinations of the link.
	# However, it is not possible to create multiple links going to the same input variable as this input cannot take more than one value, this could bring unexpected results.
	# @param varFrom A reference on the output variable where the link comes from
	# @param varTo A reference on the output variable where the link goes to
	def addLink(self, varFrom, varTo) :
		nodeFrom = varFrom.node
		nodeTo = varTo.node
		self.addLinkNode(nodeFrom, varFrom, nodeTo, varTo)

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
		if varFrom.node != nodeFrom :
			print 'Error: Node ' + nodeFrom.getName() + ' have not this var'
			return

		if varTo.node != nodeTo :
			print 'Error: Node ' + nodeTo.getName() + ' have not this var'
			return

		if varFrom.type != varTo.type :
			print 'Error: Variables have not the same type'
			return

		if not self.containLinkTo(nodeTo, varTo) :
			link = Link(nodeFrom, nodeTo, varFrom, varTo)
			nodeTo.getLinkList().append(link)
			if nodeTo != nodeFrom :
				nodeFrom.getLinkList().append(link)
			if nodeTo.getShaderType() == 0 and nodeTo != self.project.getVertexBox() and nodeFrom != self.project.getVertexBox():
				self.project.getVertexBox().getLinkList().append(link)
			elif nodeTo.getShaderType() == 1 and nodeTo != self.project.getPixelBox() and nodeFrom != self.project.getPixelBox():
				self.project.getPixelBox().getLinkList().append(link)
		else :
			print 'Error: Cannot create multiple links toward the same input var for the node ' + nodeTo.getName()

	## @fn addValuedLink(varTo, value)
	# @brief Create a link between a constant (a value) and an input variable
	# @details Creating a valuedLink allows to set an input variable as a constant, giving the value of the constant.
	# The same restriction applies on the variable destination of the link: it cannot be uses multiplie times, as a variable cannot have multiple values.
	# @param varTo A reference on the output variable where the link goes to
	# @param value The value to set
	def addValuedLink(self, varTo, value) :
		nodeTo = varTo.node
		self.addValuedLinkNode(nodeTo, varTo, value)


	## @fn addValuedLinkNode(nodeTo, varTo, value)
	# @brief Create a link between a constant (a value) and an input variable
	# @details Creating a valuedLink allows to set an input variable as a constant, giving the value of the constant.
	# The same restriction applies on the variable destination of the link: it cannot be uses multiplie times, as a variable cannot have multiple values.
	# @param nodeTo A reference on the node where to find the input variable that will be set to the given value
	# @param varTo A reference on the output variable where the link goes to
	# @param value The value to set
	def addValuedLinkNode(self, nodeTo, varTo, value) :
		find = False
		for name, var in nodeTo.getInVarList().items() :
			if var == varTo :
				find = True
				break
		if not find :
			print 'Error: Node ' + nodeTo.getName() + ' have not this input var'
			return

		if not self.containLinkTo(nodeTo, varTo) :
			link = ValuedLink(nodeTo, varTo, str(value))
			nodeTo.getLinkList().append(link)
			if nodeTo.getShaderType() == 0 and nodeTo != self.project.getVertexBox() :
				self.project.getVertexBox().getLinkList().append(link)
			elif nodeTo.getShaderType() == 1 and nodeTo != self.project.getPixelBox() :
				self.project.getPixelBox().getLinkList().append(link)
		else :
			print 'Error: Cannot create multiple links toward the same input var for the node ' + nodeTo.getName()

	## @fn addValuedLinkByName(nodeTo, nameVarTo, value)
	# @brief Create a link between a constant (a value) and an input variable
	# @details Creating a valuedLink allows to set an input variable as a constant, giving the value of the constant.
	# The same restriction applies on the variable destination of the link: it cannot be uses multiplie times, as a variable cannot have multiple values.
	# @param nodeTo A reference on the node where to find the input variable that will be set to the given value
	# @param nameVarTo The name of a reference on the output variable where the link goes to
	# @param value The value to set
	def addValuedLinkByName(self, nodeTo, nameVarTo, value) :
		varTo = None
		if nameVarTo in nodeTo.getInVarList().keys() :
			varTo = nodeTo.getInVar(nameVarTo)
		if varTo == None :
			print 'Error: Node ' + nodeTo.getName() + ' have not this input var (' + nameVarTo + ')'
			return
		if not self.containLinkTo(nodeTo, varTo) :
			link = ValuedLink(nodeTo, varTo, str(value))
			nodeTo.getLinkList().append(link)
			if nodeTo.getShaderType() == 0 and nodeTo != self.project.getVertexBox() :
				self.project.getVertexBox().getLinkList().append(link)
			elif nodeTo.getShaderType() == 1 and nodeTo != self.project.getPixelBox() :
				self.project.getPixelBox().getLinkList().append(link)
		else :
			print 'Error: Cannot create multiple links toward the same input var for the node ' + nodeTo.getName()


	## @fn deleteLink(link)
	# @brief Delete a link using its reference
	# @param link A reference on the link to delete
	def deleteLink(self, link) :
		if link.nodeFrom != None :
			link.nodeFrom.getLinkList().remove(link)
		if link.nodeTo != None :
			link.nodeTo.getLinkList().remove(link)
		if self.project.getVertexBox().getLinkList().count(link) > 0 :
			self.project.getVertexBox().getLinkList().remove(link)
		if self.project.getPixelBox().getLinkList().count(link) > 0 :
			self.project.getPixelBox().getLinkList().remove(link)

	## @fn deleteLink(nodeFrom, nodeTo, varFrom, varTo)
	# @brief Delete a link between two variables of two nodes
	# @param nodeFrom A reference on the node where to find the output variable that is linked
	# @param nodeTo A reference on the node where to find the input variable that is to this output
	# @param varFrom A reference on the output variable where the link comes from
	# @param varTo A reference on the output variable where the link goes to
	def deleteLink(self, nodeFrom, nodeTo, varFrom, varTo) :
		i = 0
		lenght = len(nodeTo.getLinkList())
		while i < lenght :
			if nodeTo.getLinkList()[i].varTo == varTo :
				link = nodeTo.getLinkList()[i]
				nodeTo.getLinkList().remove(link)
				nodeFrom.getLinkList().remove(link)
				if self.project.getVertexBox().getLinkList().count(link) > 0 :
					self.project.getVertexBox().getLinkList().remove(link)
				if self.project.getPixelBox().getLinkList().count(link) > 0 :
					self.project.getPixelBox().getLinkList().remove(link)
				return
			i += 1


	## @fn deleteValuedLink(nodeTo, varTo)
	# @brief Delete a link between a constant and a variable
	# @param nodeTo A reference on the node where to find the input variable
	# @param varTo A reference on the output variable where the link goes to
	def deleteValuedLink(self, nodeTo, varTo) :
		i = 0
		lenght = len(nodeTo.getLinkList())
		while i < lenght :
			if nodeTo.getLinkList()[i].varTo == varTo :
				if nodeTo.getLinkList()[i].nodeFrom == None :
					link = nodeTo.getLinkList().pop(i)
					if self.project.getVertexBox().getLinkList().count(link) > 0 :
						self.project.getVertexBox().getLinkList().remove(link)
					if self.project.getPixelBox().getLinkList().count(link) > 0 :
						self.project.getPixelBox().getLinkList().remove(link)
				else :
					print 'Error: Not a ValuedLink'
				return
			i += 1

	## @fn deleteAllLinkBetwinBox()
	# @brief Delete all link between the VertexBox and the PixelBox of a project
	def deleteAllLinkBetwinBox(self) :
		vertexBox = self.project.getVertexBox()
		pixelBox = self.project.getPixelBox()
		vertexLinks = self.project.getLinkList('vertex')
		pixelLinks = self.project.getLinkList('pixel')

		for link in vertexLinks :
			if (link.nodeFrom == vertexBox and link.nodeTo == pixelBox) or (link.nodeFrom == pixelBox and link.nodeTo == vertexBox) :
				vertexLinks.remove(link)
		for link in pixelLinks :
			if (link.nodeFrom == vertexBox and link.nodeTo == pixelBox) or (link.nodeFrom == pixelBox and link.nodeTo == vertexBox) :
				pixelLinks.remove(link)

	def popOneBoxLinkBetwinBox(self, box1, box2) :
		tmpLinks = []
		box1Links = box1.getLinkList()

		i = 0
		while i < len(box1Links) :
			link = box1Links[i]

			if link.nodeFrom != None and ((link.nodeFrom.getType() == 0 and link.nodeTo.getType() != 1) or (link.nodeTo.getType() == 0 and link.nodeFrom.getType() != 1)) :
				tmpLinks.append(box1Links.pop(i))
				i -= 1
			i += 1

		return tmpLinks

	## @fn addLinkListOnBox(box, linkList)
	# @brief Concatenates a new list of links to the list of links of the box given on param.
	# @param box Box which contains the list.
	# @param box The list wich will be concatenate
	def addLinkListOnBox(self, box, linkList) :
		box.setLinkList(box.getLinkList() + linkList)


	def containLinkTo(self, nodeTo, varTo) :
		i = 0
		lenght = len(nodeTo.getLinkList())
		while i < lenght :
			if nodeTo.getLinkList()[i].varTo == varTo :
				return True
			i += 1
		return False
