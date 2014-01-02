
class Gen:

	def __init__(self, params):
		self.inVars, self.outVars = params
		
	def compute(self, printer) :
		buffer = '\t' + self.outVars["color"].val + ' =  ' + self.inVars["color"].val + ' * vec4(' + self.inVars["r"].val + ', ' + self.inVars["g"].val + ', ' + self.inVars["b"].val + ', ' + self.inVars["a"].val + ');'
		buffer = buffer + '\n'
		return buffer
