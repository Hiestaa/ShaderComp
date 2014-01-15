from ..core.Shader import *

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.shaders.DefaultVertexShader
# @brief This shader will transform the world coordinates in eye-view coordinates
# @version 1.0
# @date 2014-01-07
# @shadertype Vertex Shader
# details This shader is absolutely needed at the end of any vertex shader, or the position of the object may be unexpected, or rendered objects could even desapear
# @details __Input variables:__
# - `vertex: vec4` should be linked to the pipeline input item `gl_Vertex`
# @details __Output variables:__
# - `position: vec4` should be linked to the pipeline output item `gl_Position`
# @example first_project_example.py
# @see first_project_example.py

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class DefaultVertexShader
# @brief This shader will transform the world coordinates in eye-view coordinates
# @version 1.0
# @date 2014-01-07
# @shadertype Vertex Shader
# details This shader is absolutely needed at the end of any vertex shader, or the position of the object may be unexpected, or rendered objects could even desapear
# @details __Input variables:__
# - `vertex: vec4` should be linked to the pipeline input item `gl_Vertex`
# @details __Output variables:__
# - `position: vec4` should be linked to the pipeline output item `gl_Position`
# @example first_project_example.py
# @see first_project_example.py
class DefaultVertexShader(Shader):

	## @fn __init__(self)
	# @brief Initialize this shader
	def __init__(self):
		Shader.__init__(self, 0)
		self.name = 'DefaultVertexShader'
		self.inVars['vertex'] = Var('vertex', self, VarType.IN,'vec4')
		self.outVars['position'] = Var('position', self, VarType.OUT,'vec4')
