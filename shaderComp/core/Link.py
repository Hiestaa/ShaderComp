##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.core.Link
# @brief This class is a used to link variables
# @version 1.0
# @date 2014-01-07

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class Link
# @brief This class is a Box of nodes
# @version 1.0
# @date 2014-01-07
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