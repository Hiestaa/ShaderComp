
class Gen:

	def __init__(self, params):
		self.inVars, self.outVars = params
		
	def compute(self, printer) :
		buffer = '''
		float opacity = dot(normalize(''' + self.inVars['var2'].val + '''), normalize(-''' + self.inVars['var3'].val + '''));
		opacity = abs(opacity);
		opacity = 1.0 - pow(opacity, 1);
		
		if (gl_FragColor != 0)
		{
			gl_FragColor = opacity * gl_Color * gl_FragColor;
		}
		else
		{
			gl_FragColor = opacity * gl_Color;
		}'''
		buffer = buffer + '\n'
		return buffer		
