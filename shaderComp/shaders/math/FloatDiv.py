from ...core.Shader import *
##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class FloatDiv
# @brief This shader can be used to divide an input ba another
# @version 0.1
# @date 2013-11-08
# @shadertype Fragment Shader
# @details __Input variables:__
# - `dividend: float` is the first input, that will be divided
# - `divider: float` is the second input, that will divide dividend
# @details __Output variables:__
# - `result: float` is the result of the division

class FloatDiv(Shader):

	## @fn __init__(self)
	# @brief Initialize this shader
	def __init__(self, shader_type):
		Shader.__init__(self, shader_type)
		self.name = 'FloatDiv'
		self.inVars['dividend'] = Var("dividend", self, VarType.IN,'float')
		self.inVars['divider'] = Var("divider", self, VarType.IN,'float')
		self.outVars["result"] = Var("result", self, VarType.OUT,'float')

