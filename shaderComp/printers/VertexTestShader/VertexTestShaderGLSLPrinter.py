
class Gen:

	def __init__(self, params):
		self.inVars, self.outVars = params
		
	def compute(self, printer) :
		
		buffer = '''
		//Transform vertex by modelview and projection matrices
		gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
 
		// Position in clip space
		''' + self.outVars['var1'].val + ''' = vec3(gl_ModelViewMatrix * gl_Vertex);
 
		// Normal transform (transposed model-view inverse)
		''' + self.outVars['var2'].val + ''' = gl_NormalMatrix * gl_Normal;
 
		// Incident vector
		''' + self.outVars['var3'].val + ''' = ''' + self.outVars['var1'].val + ''';
 
		// Forward current color and texture coordinates after applying texture matrix
		gl_FrontColor = gl_Color;
		gl_TexCoord[0] = gl_TextureMatrix[0] * gl_MultiTexCoord0;'''
		buffer = buffer + '\n'
		return buffer
