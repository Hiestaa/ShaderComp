from ..core.Shader import *

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class Fog
# @brief This shader will create a fog on the scene
# @version 0.1
# @date 2013-11-07
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
		Shader.__init__(self, 1)
		self.name = 'Fog'
		self.inVars['color'] = Var('color', self, VarType.IN,'vec4')
		self.inVars['fragCoord'] = Var('fragCoord', self, VarType.IN,'vec4')
		self.outVars['color'] = Var('color', self, VarType.OUT,'vec4')
