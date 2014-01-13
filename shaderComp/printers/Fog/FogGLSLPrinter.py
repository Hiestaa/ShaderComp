class Gen:
	"""Generateur du pixel shader GLSL Fog"""
	def __init__(self, params):
		self.inVars, self.outVars = params

	def compute(self, printer):
		z = printer.getRandomName('z')
		fogFactor = printer.getRandomName('fogFactor')

		buffer = '''
	float ''' + z + ''' = (''' + self.inVars['fragCoord'].val + '''.z / ''' + self.inVars['fragCoord'].val + '''.w);

	float ''' + fogFactor + ''' = log(''' + z + ''' / 25.0);
	''' + fogFactor + ''' = clamp(''' + fogFactor + ''', 0.0, 1.0);

	''' + self.outVars['color'].val + ''' = mix(''' + self.inVars['color'].val + ''', gl_Fog.color, ''' + fogFactor + ''');
'''
		return buffer

