
class Gen:

	def __init__(self, params):
		self.inVars, self.outVars = params
		
	def compute(self, printer) :
		
		buffer = '''
	''' + self.outVars['position'].val + ''' = gl_ModelViewProjectionMatrix * ''' + self.inVars['vertex'].val + ''';
'''
		return buffer
