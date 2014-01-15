##
# \authors Romain GUYOT de la HARDROUYERE
# \authors Matthieu BOURNAT
# \authors Antoine CHESNEAU
# \package shaderComp.printers.JSONPrinter
# \brief The JSONPrinter is use to export or import a project from a JSON file
# \class shaderComp.printers.JSONPrinter.Printers
# \brief The JSONPrinter is use to export or import a project from a JSON file
# \todo The compute links still needs to be implemented
# \version 0.1
# \date 2013-01-10

__name__ = "shaderComp.printers.JSONPrinter"
__package__ = "shaderComp.printers"

from ..core.Printer import *
from ..core.Render import *
import os
import json


class Printers(Printer):

	def __init__(self, projName, vertexNodeList, pixelNodeList):
		Printer.__init__(self, projName, vertexNodeList, pixelNodeList)
		self.name = 'JSONPrinter'
		self.jsonbuffer = ''
		self.indent = 0

	def render(self) :
		print 'JSON Printer Render Error: JSON is not a shader language !'

	def compute(self, project):
		print 'JSON Printer Compute: ', self.projName
		self.jsonbuffer += '{\n'
		self.indent += 1
		self.jsonbuffer += '\t"'+project.name+'":[\n'
		self.indent += 1

		self.computeNode(project.getVertexBox(), True)
		self.computeNode(project.getPixelBox(), False)
		self.jsonbuffer += '\n'

		self.jsonbuffer += '\t]\n'
		self.jsonbuffer += '}'

		self.finishCompute()

	def computeNode(self, node, first):
		if not first:
			self.jsonbuffer += ',\n'
		if node.getType() == 0 :
			self.computeBox(node)
		else:
			self.apply_indent()
			self.jsonbuffer += '"'+node.__class__.__name__+'"'

	def computeBox(self, box):
		self.apply_indent()
		self.jsonbuffer += '{\n'
		self.indent += 1
		# compute interface
		self.apply_indent()
		self.jsonbuffer += '"interface":{\n'
		self.indent += 1
		# compute input interface
		self.apply_indent()
		self.jsonbuffer += '"input":{\n'
		self.indent += 1
		first = True
		for v in box.inVars:
			self.computeVar(box.inVars[v], first)
			first = False
		self.jsonbuffer += '\n'
		self.indent -= 1
		self.apply_indent()
		self.jsonbuffer += '},\n'
		# compute output interface
		self.apply_indent()
		self.jsonbuffer += '"output":{\n'
		self.indent += 1
		first = True
		for v in box.outVars:
			self.computeVar(box.outVars[v], first)
			first = False
		self.jsonbuffer += '\n'
		self.indent -=1
		self.apply_indent()
		self.jsonbuffer += '}\n'
		# end of interface
		self.indent -= 1
		self.apply_indent()
		self.jsonbuffer += '},\n'

		# compute subnodes list
		self.apply_indent()
		self.jsonbuffer += '"nodes":[\n'
		self.indent += 1
		first = True
		for n in box.getNodeList():
			self.computeNode(n, first)
			first = False
		self.jsonbuffer += '\n'
		self.indent -= 1
		self.apply_indent()
		self.jsonbuffer += ']\n'
		# end subnodes list
		self.indent -= 1
		self.apply_indent()
		self.jsonbuffer += '}'

	def computeVar(self, var, first):
		if not first:
			self.jsonbuffer += ',\n'
		self.apply_indent()
		self.jsonbuffer += '"var":{\n'
		self.indent += 1
		self.apply_indent()
		self.jsonbuffer += '"type":"'+var.type+'",\n'
		self.apply_indent()
		self.jsonbuffer += '"name":"'+var.name+'",\n'
		self.apply_indent()
		self.jsonbuffer += '"varType":"'+str(var.varType)+'",\n'
		self.apply_indent()
		self.jsonbuffer += '"value":"'+str(var.val)+'"\n'
		self.indent -= 1
		self.apply_indent()
		self.jsonbuffer += "}"

	def apply_indent(self):
		self.jsonbuffer += ''.join(['\t' for x in range(self.indent)])

	def computeLinks(self, linkman):
		pass

	def finishCompute(self) :
		if not os.path.exists(self.projName):
			os.makedirs(self.projName)
		if self.jsonbuffer != '':
			file = open(self.projName + '/' + self.projName+'.json', 'w')
			file.write(self.jsonbuffer)
			file.close()
