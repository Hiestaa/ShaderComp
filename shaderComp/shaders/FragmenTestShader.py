from ..core.Shader import *

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.shaders.FragmenTestShader
# @brief This shader is a test of opacity
# @version 0.1
# @date 2013-11-07
# @shadertype Fragment Shader

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class FragmenTestShader
# @brief This shader is a test of opacity
# @version 0.1
# @date 2013-11-07
# @shadertype Fragment Shader
class FragmenTestShader(Shader):

	## @fn __init__(self)
	# @brief Initialize this shader
	def __init__(self):
		Shader.__init__(self, 1)
		self.name = 'FragmenTestShader'
		self.inVars['var1'] = Var('var1', self, VarType.IN,'vec3')
		self.inVars['var2'] = Var('var2', self, VarType.IN,'vec3')
		self.inVars['var3'] = Var('var3', self, VarType.IN,'vec3')
		self.inVars['edgefalloff'] = Var('edgefalloff', self, VarType.IN,'float')
