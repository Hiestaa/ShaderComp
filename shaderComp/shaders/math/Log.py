from ...core.Shader import *
##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.shaders.math.Log
# @brief This shader can be used to compute the log of a value
# @version 0.1
# @date 2013-11-08
# @shadertype Fragment Shader
# @details __Input variables:__
# - `input: float` is the input of the logarithm
# @details __Output variables:__
# - `output: float` is the result of the logarithm

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class Log
# @brief This shader can be used to compute the log of a value
# @version 0.1
# @date 2013-11-08
# @shadertype Fragment Shader
# @details __Input variables:__
# - `input: float` is the input of the logarithm
# @details __Output variables:__
# - `output: float` is the result of the logarithm

class Log(Shader):

	## @fn __init__(self)
	# @brief Initialize this shader
	def __init__(self, shader_type):
		Shader.__init__(self, shader_type)
		self.name = 'Log'
		self.inVars['input'] = Var("input", self, VarType.IN,'float')
		self.outVars["output"] = Var("output", self, VarType.OUT,'float')

