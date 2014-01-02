
class Link :

	def __init__(self, nodeFrom, nodeTo, varFrom, varTo):
		self.nodeFrom = nodeFrom
		self.nodeTo = nodeTo
		self.varFrom = varFrom
		self.varTo = varTo
		
	def printInfo(self) :
		print 'nodeFrom:', self.nodeFrom
		print 'varFrom:', self.varFrom
		print 'nodeTo:', self.nodeTo
		print 'varTo:', self.varTo