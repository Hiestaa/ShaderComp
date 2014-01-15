##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.shaders.CelShadingVertex
# @brief This shader is the vertex part of the celshading
# @version 1.0
# @date 2014-01-07
# @shadertype Vertex Shader
# @details __Input variables:__
# - `normal: vec3` is the normal of the current pixel, usually linked to the pipeline item `gl_Normal`
# @details __Output variables:__
# - `normal: vec3` is the resulting interpolated variable that is needed to be given to the `CelShadingFragment` shader
# @example first_project_example.py
# @see first_project_example.py

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class CelShadingVertex
# @brief This shader is the vertex part of the celshading
# @version 1.0
# @date 2014-01-07
# @shadertype Vertex Shader
# @details __Input variables:__
# - `normal: vec3` is the normal of the current pixel, usually linked to the pipeline item `gl_Normal`
# @details __Output variables:__
# - `normal: vec3` is the resulting interpolated variable that is needed to be given to the `CelShadingFragment` shader
# @example first_project_example.py
# @see first_project_example.py

from ..core.Shader import *

class CelShadingVertex(Shader):

	## @fn __init__(self)
	# @brief Initialize this shader
	def __init__(self):
		Shader.__init__(self, 0)
		self.name = 'CelShadingVertex'
		self.outVars['normal'] = Var('normal', self, VarType.OUT,'vec3')
		self.inVars['normal'] = Var('normal', self, VarType.IN,'vec3')

