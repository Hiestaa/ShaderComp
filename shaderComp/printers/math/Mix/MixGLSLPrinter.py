class Gen:
	"""Generateur du pixel shader mathematique Mix"""
	def __init__(self, params):
		self.inVars, self.outVars = params

	def compute(self, printer):
	
		buffer = '''
	''' + self.outVars['result'].val + ''' = mix(''' + self.inVars['v1'].val + ''', ''' + self.inVars['v2'].val + ''', ''' + self.inVars['factor'].val + ''');
'''
		return buffer

		