from Link import *
from ValuedLink import *
from Var import *

class LinkManager :
	
	def __init__(self, project):
		self.project = project
	
	def addLink(self, varFrom, varTo) :
		nodeFrom = varFrom.node
		nodeTo = varTo.node
		self.addLinkNode(nodeFrom, varFrom, nodeTo, varTo)		
	
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
			
	# def addLinkByName(self, nodeFrom, nodeTo, nameVarFrom, nameVarTo) :
		# varFrom = None
		# varTo = None
		# if nameVarFrom in nodeFrom.getOutVarList().keys() :
			# varFrom = nodeFrom.getOutVar(nameVarFrom)
		# if nameVarFrom in nodeFrom.getInVarList().keys() :
			# if varFrom != None :
				# print 'Error: Node ' + nodeFrom.getName() + ' have two var with this name (' + nameVarFrom + ')'
				# return
			# varFrom = nodeFrom.getInVar(nameVarFrom)
		# if varFrom == None :
			# print 'Error: Node ' + nodeFrom.getName() + ' have not this var (' + nameVarFrom + ')'
			# return
		# if nameVarTo in nodeTo.getInVarList().keys() :
			# varTo = nodeTo.getInVar(nameVarTo)
		# if nameVarTo in nodeTo.getOutVarList().keys() :
			# if varTo != None :
				# print 'Error: Node ' + nodeTo.getName() + ' have two var with this name (' + nameVarTo + ')'
				# return
			# varTo = nodeTo.getOutVar(nameVarTo)
		# if varTo == None :
			# print 'Error: Node ' + nodeTo.getName() + ' have not this var (' + nameVarTo + ')'
			# return
		
		# if not self.containLinkTo(nodeTo, varTo) :
			# link = Link(nodeFrom, nodeTo, varFrom, varTo)
			# nodeTo.getLinkList().append(link)
			# nodeFrom.getLinkList().append(link)
			# if nodeTo.getType() == 1 and nodeFrom.getType() == 1:
				# if nodeTo.getShaderType() == 0 :
					# self.project.getVertexBox().getLinkList().append(link)
				# elif nodeTo.getShaderType() == 1 :
					# self.project.getPixelBox().getLinkList().append(link)
		# else :
			# print 'Error: Cannot create multiple links toward the same input var for the node ' + nodeTo.getName()
	
	def addValuedLink(self, varTo, value) :
		nodeTo = varTo.node
		self.addValuedLinkNode(nodeTo, varTo, value)
	
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
			
	def deleteLink(self, link) :
		if link.nodeFrom != None :
			link.nodeFrom.getLinkList().remove(link)
		if link.nodeTo != None :
			link.nodeTo.getLinkList().remove(link)
		if self.project.getVertexBox().getLinkList().count(link) > 0 :
			self.project.getVertexBox().getLinkList().remove(link)
		if self.project.getPixelBox().getLinkList().count(link) > 0 :
			self.project.getPixelBox().getLinkList().remove(link)
	
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
			# if link.nodeFrom != None :
				# print link.nodeFrom.getName(), link.varFrom.val, link.nodeTo.getName(), link.varTo.val
			# else :
				# print link.value, link.nodeTo.getName(), link.varTo.val
			if link.nodeFrom != None and ((link.nodeFrom.getType() == 0 and link.nodeTo.getType() != 1) or (link.nodeTo.getType() == 0 and link.nodeFrom.getType() != 1)) :
				tmpLinks.append(box1Links.pop(i))
				#print 'good'
				i -= 1
			i += 1
		# for link in box1Links :
			# if link.nodeFrom != None and ((link.nodeFrom == box1 and link.nodeTo == box2) or (link.nodeFrom == box2 and link.nodeTo == box1) or (link.varFrom.varType == VarType.PIPE and link.nodeTo.getType() == 0) or (link.varTo.varType == VarType.PIPE and link.nodeFrom.getType() == 0)) :
			# if link.nodeFrom != None and ((link.nodeFrom.getType() == 0 and link.nodeTo.getType() != 1) or (link.nodeTo.getType() == 0 and link.nodeFrom.getType() != 1)) :
				# print 'good'
				# tmpLinks.append(box1Links.pop(box1Links.index(link)))
		return tmpLinks
		
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
				