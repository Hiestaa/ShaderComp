class Gen:
	"""Generateur du pixel shader GLSL CelShading"""
	def __init__(self, params):
		self.inVars, self.outVars = params

	def compute(self, printer):
		print self.outVars['color'].val
		print self.inVars['color'].val
		intensity = printer.getRandomName('intensity')
		buffer = '''
	float ''' + intensity + ''';
	vec4 ''' + self.outVars['color'].val + ''';
	vec3 n = normalize(''' + self.inVars['normal'].val + ''');
	
	''' + intensity + ''' = dot(vec3(gl_LightSource[0].position),n);
	
	if (''' + intensity + ''' > 0.95)
		''' + self.outVars['color'].val + ''' = vec4(''' + self.inVars['color'].val + '''.x,''' + self.inVars['color'].val + '''.y,''' + self.inVars['color'].val + '''.z,1.0);
	else if (''' + intensity + ''' > 0.5)
		''' + self.outVars['color'].val + ''' = vec4(''' + self.inVars['color'].val + '''.x / 2.0,''' + self.inVars['color'].val + '''.y / 2.0,''' + self.inVars['color'].val + '''.z / 2.0,1.0);
	else if (''' + intensity + ''' > 0.25)
		''' + self.outVars['color'].val + ''' = vec4(''' + self.inVars['color'].val + '''.x / 4.0,''' + self.inVars['color'].val + '''.y / 4.0,''' + self.inVars['color'].val + '''.z / 4.0,1.0);
	else
		''' + self.outVars['color'].val + ''' = vec4(''' + self.inVars['color'].val + '''.x / 8.0,''' + self.inVars['color'].val + '''.y / 8.0,''' + self.inVars['color'].val + '''.z / 8.0,1.0);
'''
		return buffer

		