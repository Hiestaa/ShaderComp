class Gen:
	"""Generateur du pixel shader mathematique Log"""
	def __init__(self, params):
		self.inVars, self.outVars = params

	def compute(self, printer):
	
		buffer = '''
	''' + self.outVars['output'].val + ''' = log(''' + self.inVars['input'].val + ''');
'''
		return buffer

		