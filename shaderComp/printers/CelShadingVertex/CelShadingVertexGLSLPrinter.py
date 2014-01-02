class Gen:
	"""Generateur du pixel shader GLSL CelShading"""
	def __init__(self, params):
		self.inVars, self.outVars = params

	def compute(self, printer):
		#self.outVars['normal'].val='gl_Normal'
		buffer = '''
	''' + self.outVars['normal'].val + ''' = gl_NormalMatrix * ''' + self.inVars['normal'].val + ''';
'''
		return buffer

		