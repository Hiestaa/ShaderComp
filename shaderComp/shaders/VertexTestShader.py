from ..core.Shader import *
##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.shaders.VertexTestShader
# @brief This shader is a test of opacity
# @version 0.1
# @date 2013-11-07
# @shadertype Vertex Shader

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class VertexTestShader
# @brief This shader is a test of opacity
# @version 0.1
# @date 2013-11-07
# @shadertype Vertex Shader
class VertexTestShader(Shader):

	## @fn __init__(self)
	# @brief Initialize this shader
	def __init__(self):
		Shader.__init__(self, 0)
		self.name = 'VertexTestShader'
		self.outVars['var1'] = Var('var1', self, VarType.OUT, 'vec3')
		self.outVars['var2'] = Var('var2', self, VarType.OUT, 'vec3')
		self.outVars['var3'] = Var('var3', self, VarType.OUT, 'vec3')
