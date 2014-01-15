
##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class VarType
# @brief This shader can be used to create a new color
# @details __Variables:__
# - `IN: int` is the value for an invar (0)
# - `OUT: int` is the value for an invar (1)
# - `UNI: int` is the value for an invar (2)
# - `PIPE: int` is the value for an invar (4)
# - `VALUED: int` is the value for an invar (5)

class VarType :
	IN = 0
	OUT = 1
	UNI = 2
	PIPE = 4
	VALUED = 5


##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.core.Var
# @brief This class represent a variable
# @version 1.0
# @date 2014-01-13
# @details It can be a Uniform, a Varying as well as an input or output variable, depending on the specified type

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class Var
# @brief This class represent a variable
# @version 1.0
# @date 2014-01-13
# @details It can be a Uniform, a Varying as well as an input or output variable, depending on the specified type
class Var :

	## @fn __init__(name, node, varType, type, val)
	# @brief Instanciate an new Var
	# @param name Give a name to this variable.
	# @param node The node where the variable is.
	# @param varType An int (Vartype) specifying the vartype of the variable:
	# - `IN`: 0
	# - `OUT`: 1
	# - `UNI`: 2
	# - `PIPE`: 4
	# - `VALUED`: 5
	# @param type A string specifying the type of the variable. Supported valued are all the GLSL commonly used variable types.
	# @param val The value of the Var of type specified in "type" param.
	def __init__(self, name, node, varType, type=None, val=None):
		self.val = val
		self.type = type
		self.varType = varType
		self.node = node
		self.name = name
