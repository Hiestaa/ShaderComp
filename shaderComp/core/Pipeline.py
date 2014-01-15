from Var import *

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.core.Pipeline
# @brief This class represent the graphics pipeline and holds all te corresponding variables
# @version 1.0
# @date 2014-01-13
# @details Here is the list of pipeline variables available:
# 		- 'Vertex': 	equivalent to gl_Vertex in glsl
#		- 'Normal': 	equivalent to gl_Normal in glsl
#		- 'Position': 	equivalent to gl_Position in glsl
#		- 'Color': 		equivalent to gl_Color in glsl
#		- 'FragColor': 	equivalent to gl_FragColor in glsl
#		- 'FragCoord': 	equivalent to gl_FragCoord in glsl
#		- 'FogColor':	equivalent to gl_Fog.color in glsl

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class Pipeline
# @brief This class represent the graphics pipeline and holds all te corresponding variables
# @version 1.0
# @date 2014-01-13
# @details Here is the list of pipeline variables available:
# 		- 'Vertex': 	equivalent to gl_Vertex in glsl
#		- 'Normal': 	equivalent to gl_Normal in glsl
#		- 'Position': 	equivalent to gl_Position in glsl
#		- 'Color': 		equivalent to gl_Color in glsl
#		- 'FragColor': 	equivalent to gl_FragColor in glsl
#		- 'FragCoord': 	equivalent to gl_FragCoord in glsl
#		- 'FogColor':	equivalent to gl_Fog.color in glsl


class Pipeline :
	@staticmethod
	def getPipelineVars(node) :
		pipelineVars = {}
		pipelineVars['Vertex'] = Var('Vertex', node, VarType.PIPE, 'vec4', 'gl_Vertex')
		pipelineVars['Normal'] = Var('Normal', node, VarType.PIPE, 'vec3', 'gl_Normal')
		pipelineVars['Position'] = Var('Position', node, VarType.PIPE, 'vec4', 'gl_Position')
		pipelineVars['Color'] = Var('Color', node, VarType.PIPE, 'vec4', 'gl_Color')
		pipelineVars['FragColor'] = Var('FragColor', node, VarType.PIPE, 'vec4', 'gl_FragColor')
		pipelineVars['FragCoord'] = Var('FragCoord', node, VarType.PIPE, 'vec4', 'gl_FragCoord')
		pipelineVars['FogColor'] = Var('FogColor', node, VarType.PIPE, 'vec4', 'gl_Fog.color')
		return pipelineVars