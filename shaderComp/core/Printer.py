
##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.core.Printer
# @brief This class is the parent class of all the Printers
# @version 1.0
# @date 2014-01-07
# @details This class provides features allowing to easily developp new plugins Printers.

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class Printer
# @brief This class is the parent class of all the Printers
# @version 1.0
# @date 2014-01-07
# @details This class provides features allowing to easily developp new plugins Printers.

import imp
import time
from Var import *

class Printer:

	def __init__(self, projName, vertexNodeList, pixelNodeList):
		self.projName = projName
		self.vertexNodeList = vertexNodeList
		self.pixelNodeList = pixelNodeList
		self.vertexShaderBuffer = ''
		self.fragmentShaderBuffer = ''
		self.nbDec = -1
		self.vertexDeclaration = {}
		self.fragmentDeclaration = {}

		self.language_types = {}

	def compute(self, project) :
		pass

	def getRandomName(self, seed) :
		self.nbDec += 1
		return str(seed) + str(self.nbDec) + '_' + str(int(time.time()) % 10000)

	def applyVarNameSelection(self, project) :
		vertexLinks = project.getLinkList('vertex')
		pixelLinks = project.getLinkList('pixel')

		for link in vertexLinks :
			if link.nodeFrom == None :
				link.varTo.val = link.value
				link.varTo.varType = VarType.VALUED
			if link.nodeFrom != None :
				if link.varFrom.varType == VarType.PIPE or link.varFrom.varType == VarType.UNI:
					link.varTo.varType = link.varFrom.varType
					link.varTo.val = link.varFrom.val
				if link.varTo.varType == VarType.PIPE or link.varTo.varType == VarType.UNI :
					link.varFrom.varType = link.varTo.varType
					link.varFrom.val = link.varTo.val

		for link in vertexLinks :
			if link.nodeFrom == None : # valued link
				link.varTo.val = link.value
			else :
				if link.varFrom.val != None : # deja ete rempli (uniform, ou sortie dupliquee)
					link.varTo.val = link.varFrom.val
				elif link.varTo.val != None : # deja ete rempli (uniform, ou sortie dupliquee)
					link.varFrom.val = link.varTo.val

				else : # construction du nom
					self.nbDec += 1
					name = link.varFrom.name + str(self.nbDec) + '_' + str(int(time.time()) % 10000)
					link.varTo.val = name
					link.varFrom.val = name

				if link.varFrom.varType == VarType.PIPE or link.varTo.varType == VarType.PIPE or link.varFrom.varType == VarType.VALUED or link.varTo.varType == VarType.VALUED:
					continue

				if link.nodeFrom.getType() == 0 : # le lien vient d'une entree de la box
					if link.varFrom.varType == VarType.UNI : # si uniform
						self.addDeclaration(0, ('uniform', self.language_types[link.varFrom.type]), link.varFrom.val)
					else : # non
						self.addDeclaration(0, ('varying', self.language_types[link.varFrom.type]), link.varFrom.val)
				elif link.nodeTo.getType() == 0 : # le lien va vers une sortie de la box
					if link.varTo.varType == VarType.UNI : # si uniform
						self.addDeclaration(0, ('uniform', self.language_types[link.varTo.type]), link.varTo.val)
					else : #non
						self.addDeclaration(0, ('varying', self.language_types[link.varTo.type]), link.varTo.val)
				else :
					self.addDeclaration(0, (None , self.language_types[link.varTo.type]), link.varTo.val)


		for link in pixelLinks :
			if link.nodeFrom == None :
				link.varTo.val = link.value
				link.varTo.varType = VarType.VALUED
			if link.nodeFrom != None :
				if link.varFrom.varType == VarType.PIPE or link.varFrom.varType == VarType.UNI:
					link.varTo.varType = link.varFrom.varType
					link.varTo.val = link.varFrom.val
				if link.varTo.varType == VarType.PIPE or link.varTo.varType == VarType.UNI :
					link.varFrom.varType = link.varTo.varType
					link.varFrom.val = link.varTo.val

		for link in pixelLinks :
			if link.nodeFrom == None :
				link.varTo.val = link.value
			else :
				if link.varFrom.val != None :
					link.varTo.val = link.varFrom.val
				elif link.varTo.val != None : # deja ete rempli (uniform, ou sortie dupliquee)
					link.varFrom.val = link.varTo.val
				else :
					self.nbDec += 1
					name = link.varFrom.name + str(self.nbDec) + '_' + str(int(time.time()) % 10000)
					link.varTo.val = name
					link.varFrom.val = name


				if link.varFrom.varType == VarType.PIPE or link.varTo.varType == VarType.PIPE or link.varFrom.varType == VarType.VALUED or link.varTo.varType == VarType.VALUED:
					continue


				if link.nodeFrom.getType() == 0 :
					if link.varFrom.varType == VarType.UNI : # si uniform :
						self.addDeclaration(1, ('uniform', self.language_types[link.varFrom.type]), link.varFrom.val)
					else :
						self.addDeclaration(1, ('varying', self.language_types[link.varFrom.type]), link.varFrom.val)
				elif link.nodeTo.getType() == 0 :
					if link.varTo.varType == VarType.UNI : # si uniform :
						self.addDeclaration(1, ('uniform', self.language_types[link.varTo.type]), link.varTo.val)
					else :
						self.addDeclaration(1, ('varying', self.language_types[link.varTo.type]), link.varTo.val)
				else :
					self.addDeclaration(1, (None , self.language_types[link.varTo.type]), link.varTo.val)

	def removeAllVarName(self, project) :
		vertexLinks = project.getLinkList('vertex')
		pixelLinks = project.getLinkList('pixel')
		for link in vertexLinks :
			if link.nodeFrom != None and (link.nodeFrom.getType() == 1 or (link.varFrom.varType != VarType.UNI and link.varFrom.varType != VarType.PIPE)) :
				link.varFrom.val = None
			if link.nodeTo != None and (link.nodeTo.getType() == 1 or (link.varTo.varType != VarType.UNI and link.varTo.varType != VarType.PIPE)) :
				link.varTo.val = None
		for link in pixelLinks :
			if link.nodeFrom != None and (link.nodeFrom.getType() == 1 or (link.varFrom.varType != VarType.UNI and link.varFrom.varType != VarType.PIPE)) :
				link.varFrom.val = None
			if link.nodeTo != None and (link.nodeTo.getType() == 1 or (link.varTo.varType != VarType.UNI and link.varTo.varType != VarType.PIPE)) :
				link.varTo.val = None

	def addDeclaration(self, shaderType, declaration, name) :
		if shaderType == 0 :
			if name not in self.vertexDeclaration :
				self.vertexDeclaration[name] = declaration
			elif declaration[0] != None :
				self.vertexDeclaration[name] = declaration
		elif shaderType == 1 :
			if name not in self.fragmentDeclaration :
				self.fragmentDeclaration[name] = declaration
			elif declaration[0] != None :
				self.fragmentDeclaration[name] = declaration

