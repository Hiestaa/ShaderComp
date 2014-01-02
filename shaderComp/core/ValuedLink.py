
class ValuedLink :

	def __init__(self, nodeTo, varTo, value):
		self.nodeTo = nodeTo
		self.varTo = varTo
		self.value = value
		self.nodeFrom = None
		
	def printInfo(self) :
		print 'nodeFrom:', self.nodeFrom
		print 'nodeTo:', self.nodeTo
		print 'varTo:', self.varTo
		print 'value:', self.value
		