from ...core.Shader import *
##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class Mix
# @brief This shader can be used to mix two vectors of type float4 within a given factor
# @version 0.1
# @date 2013-11-08
# @shadertype Fragment Shader
# @details __Input variables:__
# - `v1: vec4` is the first input vector
# - `v2: vec4` is the second input vector
# - `factor: float` the mix factor between 0.0 and 1.0. If the factor is big the result will be near the vector v2.
#       If the factor is low, the result will be near the vector v1.
# @details __Output variables:__
# - `result: float` is the result of the operation
# @details The resulting operation will be something like `result = mix(v1, v2, factor)`

class Mix(Shader):

	## @fn __init__(self)
	# @brief Initialize this shader
	def __init__(self, shader_type):
		Shader.__init__(self, shader_type)
		self.name = 'Mix'
		self.inVars['v1'] = Var("v1", self, VarType.IN,'vec4')
		self.inVars['v2'] = Var("v2", self, VarType.IN,'vec4')
		self.inVars['factor'] = Var("factor", self, VarType.IN,'float')
		self.outVars["result"] = Var("result", self, VarType.OUT,'vec4')



