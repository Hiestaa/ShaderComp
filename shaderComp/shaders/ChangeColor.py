from ..core.Shader import *
##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.shaders.ChangeColor
# @brief This shader can be used to mix an input color and a predefined second color
# @version 1.0
# @date 2014-01-07
# @shadertype Fragment Shader
# @details __Input variables:__
# - `color: vec4` is the input color that will be mixed
# - `r: float` is the r component of the mixing color
# - `g: float` is the g component of the mixing color
# - `b: float` is the b component of the mixing color
# - `a: float` is the a component of the mixing color
# @details __Output variables:__
# - `normal: vec4` is the resulting color
# @example first_project_example.py
# @example shader_link_example.py
# Here is an example of how to link two shaders in a project.
# @see first_project_example.py
# @see shader_link_example.py
# @todo take a vec4 as input instead of 4 float


##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class ChangeColor
# @brief This shader can be used to mix an input color and a predefined second color
# @version 1.0
# @date 2013-11-07
# @shadertype Fragment Shader
# @details __Input variables:__
# - `color: vec4` is the input color that will be mixed
# - `r: float` is the r component of the mixing color
# - `g: float` is the g component of the mixing color
# - `b: float` is the b component of the mixing color
# - `a: float` is the a component of the mixing color
# @details __Output variables:__
# - `normal: vec4` is the resulting color
# @example first_project_example.py
# @example shader_link_example.py
# Here is an example of how to link two shaders in a project.
# @see first_project_example.py
# @see shader_link_example.py
# @todo take a vec4 as input instead of 4 float

class ChangeColor(Shader):

	## @fn __init__(self)
	# @brief Initialize this shader
	def __init__(self):
		Shader.__init__(self, 1)
		self.name = 'ChangeColor'
		self.inVars["r"] = Var("r", self, VarType.IN,'float')
		self.inVars["g"] = Var("g", self, VarType.IN,'float')
		self.inVars["b"] = Var("b", self, VarType.IN,'float')
		self.inVars["a"] = Var("a", self, VarType.IN,'float')
		self.inVars['color'] = Var("color", self, VarType.IN,'vec4')
		self.outVars['color'] = Var("color", self, VarType.OUT,'vec4')

	## @fn setR(self,r)
	# @brief Allows to link the `r` input variable to a constant
	# @details This function will build the valuedLink needed for you.
	# @param r The constant value of this input variable
	def setR(self, r) :
		if self.linkManager == None :
			print 'Add Node on Project Before'
		else :
			self.linkManager.addValuedLink(self, self.inVars["r"], r)

	## @fn setG(self,g)
	# @brief Allows to link the `g` input variable to a constant
	# @details This function will build the valuedLink needed for you.
	# @param g The constant value of this input variable
	def setG(self, g) :
		if self.linkManager == None :
			print 'Add Node on Project Before'
		else :
			self.linkManager.addValuedLink(self, self.inVars["g"], g)

	## @fn setB(self,b)
	# @brief Allows to link the `b` input variable to a constant
	# @details This function will build the valuedLink needed for you.
	# @param b The constant value of this input variable
	def setB(self, b) :
		if self.linkManager == None :
			print 'Add Node on Project Before'
		else :
			self.linkManager.addValuedLink(self, self.inVars["b"], b)

	## @fn setA(self,a)
	# @brief Allows to link the `a` input variable to a constant
	# @details This function will build the valuedLink needed for you.
	# @param a The constant value of this input variable
	def setA(self, a) :
		if self.linkManager == None :
			print 'Add Node on Project Before'
		else :
			self.linkManager.addValuedLink(self, self.inVars["a"], a)

	## @fn setParams(self,r, g, b, a)
	# @brief Allows to link the `r`, `g`, `b` and `a` input variables to constants
	# @details This function will build the valuedLinks needed for you.
	# @param r The constant value of this input variable
	# @param g The constant value of this input variable
	# @param b The constant value of this input variable
	# @param a The constant value of this input variable
	def setParams(self, r, g, b, a) :
		if self.linkManager == None :
			print 'Add Node on Project Before'
		else :
			self.linkManager.addValuedLink(self, self.inVars["r"], r)
			self.linkManager.addValuedLink(self, self.inVars["g"], g)
			self.linkManager.addValuedLink(self, self.inVars["b"], b)
			self.linkManager.addValuedLink(self, self.inVars["a"], a)
