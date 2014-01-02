from ..core.Shader import *
##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class CelShadingFragment
# @brief This shader is the fragment part of the celshading
# @version 0.1
# @date 2013-11-07
# @shadertype Fragment Shader
# @details __Input variables:__
# - `normal: vec3` is the interpolated normal of the surface displayed by the current pixel
# - `color: vec4` is the color of the pixel that will be modified
# @details __Output variables:__ 
# - `color: vec4` is the resulting color of the pixel after the cel shading is processed
# @example first_project_example.py
# @see first_project_example.py

class CelShadingFragment(Shader):

	## @fn __init__(self)
	# @brief Initialize this shader
	def __init__(self):
		Shader.__init__(self, 1)
		self.name = 'CelShadingFragment'
		self.inVars['normal'] = Var('normal', self, VarType.IN, 'vec3')
		self.outVars['color'] = Var('color', self, VarType.OUT,'vec4')
		self.inVars['color'] = Var('color', self, VarType.IN,'vec4')
