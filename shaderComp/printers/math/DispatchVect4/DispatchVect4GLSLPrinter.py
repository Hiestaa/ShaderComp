class Gen:
	"""Generateur du pixel shader mathematique DispatchVect4"""
	def __init__(self, params):
		self.inVars, self.outVars = params

	def compute(self, printer):
	
		buffer = '''
	'''
		# si le lien avec la variable d'entree est fait
		if self.inVars['myVec4'].val:
			if self.outVars['x'].val:
				buffer += self.outVars['x'].val + ''' = ''' + self.inVars['myVec4'].val + '''.x;
	'''		
			if self.outVars['y'].val:
				buffer += self.outVars['y'].val + ''' = ''' + self.inVars['myVec4'].val + '''.y;
	'''	
			if self.outVars['z'].val:
				buffer += self.outVars['z'].val + ''' = ''' + self.inVars['myVec4'].val + '''.z;
	'''	
			if self.outVars['w'].val:
				buffer += self.outVars['w'].val + ''' = ''' + self.inVars['myVec4'].val + '''.w;
'''
		return buffer

		