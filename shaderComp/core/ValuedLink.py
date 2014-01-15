
##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.core.ValuedLink
# @brief Represent a link with input value is a constant
# @version 1.0
# @date 2014-01-13

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class ValuedLink
# @brief Represent a link with input value is a constant
# @version 1.0
# @date 2014-01-13

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
