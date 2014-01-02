from Var import *

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