
class VarType :
	IN = 0
	OUT = 1
	UNI = 2
	PIPE = 4
	VALUED = 5

class Var :
	
	def __init__(self, name, node, varType, type=None, val=None):
		self.val = val
		self.type = type
		self.varType = varType
		self.node = node
		self.name = name
		