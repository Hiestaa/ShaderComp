##
# \authors Romain GUYOT de la HARDROUYERE
# \authors Matthieu BOURNAT
# \authors Antoine CHESNEAU
# \brief This example show the use of the library for the creation of a fog shader.
# \version 0.1
# \date 2013-11-08
# \details Remember that a box is a node, as a shader is, with its input and output variable.
#    This allow to create the same fog shader as already built-in,
#    but using only low-level mathematics functions like divide or logarithm.
#    This is the purpose of this example
# \todo TODO: les entrees 'color' et 'fogFactor' de la box doivent etre liees a une constante.
#   Pour l'instant ca ne marche pas, je suis oblige de lier directement l'entree du shader avec le valued link,
#	sinon un 'varying' est genere, et la constante n'est pas assignee

from shaderComp.core import *
from shaderComp.shaders import *
from shaderComp.shaders.math import *

# creation du projet 'myFog'
myFogProject = Project.Project('myFog')

# creation des noeuds
myDefaultVertexShader = DefaultVertexShader.DefaultVertexShader()
myDispatchVect4 = DispatchVect4.DispatchVect4(ShaderType.PIXEL_SHADER)
myFloatDiv1 = FloatDiv.FloatDiv(ShaderType.PIXEL_SHADER)
myFloatDiv2 = FloatDiv.FloatDiv(ShaderType.PIXEL_SHADER)
myLog = Log.Log(ShaderType.PIXEL_SHADER)
myClamp = Clamp.Clamp(ShaderType.PIXEL_SHADER)
myMix = Mix.Mix(ShaderType.PIXEL_SHADER)

# ajout des noeuds au projet
myFogProject.appendNode(myDefaultVertexShader)
myFogProject.appendNode(myDispatchVect4)
myFogProject.appendNode(myFloatDiv1)
myFogProject.appendNode(myFloatDiv2)
myFogProject.appendNode(myLog)
myFogProject.appendNode(myClamp)
myFogProject.appendNode(myMix)

# setting the input variables to a constant
myFogProject.addValuedLink(myClamp.getInVar('min'), 0.0)
myFogProject.addValuedLink(myClamp.getInVar('max'), 1.0)

# creation des variables d'entree et de sortie du la vertex box
vertexOutFinalPositionVar = myFogProject.addVertexOutVar('final_position', 'vec4')
vertexInVertVar = myFogProject.addVertexInVar('vertex', 'vec4')

# creation des variables d'entree et de sortie de la pixel box
pixelInFragCoordVar = myFogProject.addPixelInVar('fragCoord', 'vec4')
pixelInColorVar = myFogProject.addPixelInVar('color', 'vec4')
pixelInFogFactorVar = myFogProject.addPixelInVar('fogFactor', 'float')
pixelInFogColorVar = myFogProject.addPixelInVar('fogColor', 'vec4')
pixelOutFinalColor = myFogProject.addPixelOutVar('color', 'vec4')

# creation des liens entre pipeline et etrees des box
myFogProject.addLink(myFogProject.getVertexPipelineVar('Vertex'), vertexInVertVar)
myFogProject.addLink(myFogProject.getPixelPipelineVar('FragCoord'), pixelInFragCoordVar)
myFogProject.addLink(myFogProject.getPixelPipelineVar('FogColor'), pixelInFogColorVar)

# creation des liens entre pipeline et sorties des box
myFogProject.addLink(vertexOutFinalPositionVar, myFogProject.getVertexPipelineVar('Position'))
myFogProject.addLink(pixelOutFinalColor, myFogProject.getPixelPipelineVar('FragColor'))

# creation des liens entre les variables d'entree/sortie de la vertex box et les shaders qu'elle contient
myFogProject.addLink(vertexInVertVar, myDefaultVertexShader.getInVar('vertex'))
myFogProject.addLink(myDefaultVertexShader.getOutVar('position'), vertexOutFinalPositionVar)

# creation des liens entre les variables d'entree/sortie de la pixel box et les shaders qu'elle contient
myFogProject.addLink(pixelInFragCoordVar, myDispatchVect4.getInVar('myVec4'))
myFogProject.addLink(myDispatchVect4.getOutVar('z'), myFloatDiv1.getInVar('dividend'))
myFogProject.addLink(myDispatchVect4.getOutVar('w'), myFloatDiv1.getInVar('divider'))
myFogProject.addLink(myFloatDiv1.getOutVar('result'), myFloatDiv2.getInVar('dividend'))
myFogProject.addLink(pixelInFogFactorVar, myFloatDiv2.getInVar('divider'))
myFogProject.addLink(myFloatDiv2.getOutVar('result'), myLog.getInVar('input'))
myFogProject.addLink(myLog.getOutVar('output'), myClamp.getInVar('value'))
myFogProject.addLink(myClamp.getOutVar('result'), myMix.getInVar('factor'))
myFogProject.addLink(pixelInColorVar, myMix.getInVar('v1'))
myFogProject.addLink(pixelInFogColorVar, myMix.getInVar('v2'))
myFogProject.addLink(myMix.getOutVar('result'), pixelOutFinalColor)




# creation des liens values = assignation des valeurs constantes aux entrees de la pixel box
#myFogProject.addValuedLink(pixelInColorVar, 'vec4(0.5, 0.5, 1.0, 1.0)') #relink dans main2 alors que supprime pas les linkedLink, a commenter pour creer un fog viable
myFogProject.addValuedLink(pixelInFogFactorVar, 25.0)

myFogProject.saveBox('fog', 'pixel')


#myFogProject.compute()
#myFogProject.render() # assert que le fog fonctionne