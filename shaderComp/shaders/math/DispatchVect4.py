from ...core.Shader import *
##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class DispatchVect4
# @brief This shader can be used to get the component of a vector
# @version 0.1
# @date 2013-11-08
# @shadertype Fragment Shader
# @details __Input variables:__
# - `myVec4: vec4` is the vector to dispatch
# @details __Output variables:__
# - `x: float` is the x component of the vector
# - `y: float` is the y component of the vector
# - `z: float` is the z component of the vector
# - `w: float` is the w component of the vector

class DispatchVect4(Shader):

	## @fn __init__(self)
	# @brief Initialize this shader
	def __init__(self, shader_type):
		Shader.__init__(self, shader_type)
		self.name = 'DispatchVect4'
		self.inVars['myVec4'] = Var("myVec4", self, VarType.IN,'vec4')
		self.outVars["x"] = Var("x", self, VarType.OUT,'float')
		self.outVars["y"] = Var("y", self, VarType.OUT,'float')
		self.outVars["z"] = Var("z", self, VarType.OUT,'float')
		self.outVars["w"] = Var("w", self, VarType.OUT,'float')

