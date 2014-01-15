from ..core.Shader import *
from ..core.ShaderType import *
##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.shaders.Fog
# @brief This shader will create a fog on the scene
# @version 1.0
# @date 2014-01-07
# @shadertype Fragment Shader
# details It will use the fragment coordinates to evaluate the depth
# of the surface corresponding to this pixel, then modify the pixel color
# to make it disapear if it's too far from the point of view
# @details __Input variables:__
# - `frag_coord: vec4` should be linked to the pipeline input item `gl_FragCoord`
# - `color: vec4` is the color of the current pixel
# @details __Output variables:__
# - `color: vec4` the resulting color after applying the fog
# @example first_project_example.py
# @see first_project_example.py

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class Fog
# @brief This shader will create a fog on the scene
# @version 1.0
# @date 2014-01-07
# @shadertype Fragment Shader
# details It will use the fragment coordinates to evaluate the depth
# of the surface corresponding to this pixel, then modify the pixel color
# to make it disapear if it's too far from the point of view
# @details __Input variables:__
# - `frag_coord: vec4` should be linked to the pipeline input item `gl_FragCoord`
# - `color: vec4` is the color of the current pixel
# @details __Output variables:__
# - `color: vec4` the resulting color after applying the fog
# @example first_project_example.py
# @see first_project_example.py
class Fog(Shader):

	## @fn __init__(self)
	# @brief Initialize this shader
	def __init__(self):
		Shader.__init__(self, ShaderType.PIXEL_SHADER)
		self.inVars['color'] = Var('color', self, VarType.IN,'vec4')
		self.inVars['fragCoord'] = Var('fragCoord', self, VarType.IN,'vec4')
		self.outVars['color'] = Var('color', self, VarType.OUT,'vec4')
		self.name = 'Fog'
