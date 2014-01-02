class Gen:
	"""Generateur du pixel shader mathematique Clamp"""
	def __init__(self, params):
		self.inVars, self.outVars = params

	def compute(self, printer):
	
		buffer = '''
	''' + self.outVars['result'].val + ''' = clamp(''' + self.inVars['value'].val + ''', ''' + self.inVars['min'].val + ''', ''' + self.inVars['max'].val + ''');
'''
		return buffer

		