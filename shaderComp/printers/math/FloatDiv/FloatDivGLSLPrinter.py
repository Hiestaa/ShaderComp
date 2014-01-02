class Gen:
	"""Generateur du pixel shader mathematique FloatDiv"""
	def __init__(self, params):
		self.inVars, self.outVars = params

	def compute(self, printer):
	
		buffer = '''
	''' + self.outVars['result'].val + ''' = ''' \
		+ self.inVars['dividend'].val + ''' / ''' \
		+ self.inVars['divider'].val + ''';
'''
		return buffer

		