from ...core.Shader import *
##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class Clamp
# @brief This shader can be used to limit a value with a maximum and a minimum
# @version 0.1
# @date 2013-11-08
# @shadertype Fragment Shader
# @details __Input variables:__
# - `value: float` is the input value that will be limited
# - `min: float` is the minimum the value can take
# - `max: float` is the maximum the value can take
# @details __Output variables:__ 
# - `result: float` is the result of the operation

class Clamp(Shader):

	## @fn __init__(self)
	# @brief Initialize this shader
	def __init__(self):
		Shader.__init__(self, 1)
		self.name = 'Clamp'
		self.inVars['value'] = Var("value", self, VarType.IN,'float')
		self.inVars['min'] = Var("min", self, VarType.IN,'float')
		self.inVars['max'] = Var("max", self, VarType.IN,'float')
		self.outVars["result"] = Var("result", self, VarType.OUT,'float')

	## @fn setMin(mini)
	# @brief Allows to link the `min` input variable to a constant
	# @details This function will build the valuedLink needed for you.	
	# @param mini The constant value of this input variable
	def setMin(self, mini) :
		if self.linkManager == None :
			print 'Add Node on Project Before'
		else :
			self.linkManager.addValuedLink(self.inVars["min"], mini)
		
	## @fn setG(self,maxi)
	# @brief Allows to link the `maxi` input variable to a constant
	# @details This function will build the valuedLink needed for you.	
	# @param maxi The constant value of this input variable
	def setMax(self, maxi) :
		if self.linkManager == None :
			print 'Add Node on Project Before'
		else :
			self.linkManager.addValuedLink(self.inVars["max"], maxi)
		
	
