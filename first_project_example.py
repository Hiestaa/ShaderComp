##
# \authors Romain GUYOT de la HARDROUYERE
# \authors Matthieu BOURNAT
# \authors Antoine CHESNEAU
# \brief This example show the use of the library for the constitution of a small shader assembly
# \version 0.1
# \date 2013-11-08
# \details The project contains a color shader that will set the color,
#   a 'change color' shader that will edit the first color, a celshading process
#   and a fog shader. Note that the 'color' and the 'change color' are not realy useful,
#   but are used here for the demonstration.


from shaderComp.core import *
from shaderComp.shaders import *

myProj = Project.Project('TestProj')

# creation des shaders
myColor = Color.Color()
myChangeColor = ChangeColor.ChangeColor()
myCelShadingVertex = CelShadingVertex.CelShadingVertex()
myCelShadingFragment = CelShadingFragment.CelShadingFragment()
myDefaultVertexShader = DefaultVertexShader.DefaultVertexShader()
myFog = Fog.Fog()

# ajout des noeuds au projet
myProj.appendNode(myColor)
myProj.appendNode(myChangeColor)
myProj.appendNode(myCelShadingVertex)
myProj.appendNode(myCelShadingFragment)
myProj.appendNode(myDefaultVertexShader)
myProj.appendNode(myFog)

# creation des variables d'entree et de sortie du la vertex box
vertexOutNormalVar = myProj.addVertexOutVar('normal', 'vec3')
vertexOutFinalPositionVar = myProj.addVertexOutVar('final_position', 'vec4')
vertexInVertVar = myProj.addVertexInVar('vertex', 'vec4')
vertexInNormalVar = myProj.addVertexInVar('normal', 'vec3')

# creation des variables d'entree et de sortie de la pixel box
pixelInNormalVar = myProj.addPixelInVar('normal', 'vec3')
pixelInFragCoordVar = myProj.addPixelInVar('fragCoord', 'vec4')
pixelOutFinalColor = myProj.addPixelOutVar('final_color', 'vec4')

myProj.addLink(myProj.getVertexPipelineVar('Vertex'), vertexInVertVar)
myProj.addLink(myProj.getVertexPipelineVar('Normal'), vertexInNormalVar)
myProj.addLink(myProj.getVertexPipelineVar('FragCoord'), pixelInFragCoordVar)

myProj.addLink(vertexOutFinalPositionVar, myProj.getVertexPipelineVar('Position'))
myProj.addLink(pixelOutFinalColor, myProj.getPixelPipelineVar('FragColor'))

# creation des liens entre les variables d'entree/sortie de la vertex box et les shaders qu'elle contient
myProj.addLink(vertexInVertVar, myDefaultVertexShader.getInVar('vertex'))
myProj.addLink(vertexInNormalVar, myCelShadingVertex.getInVar('normal'))
myProj.addLink(myDefaultVertexShader.getOutVar('position'), vertexOutFinalPositionVar)
myProj.addLink(myCelShadingVertex.getOutVar('normal'), vertexOutNormalVar)

# creation des liens values = assignation d'une valeur aux entree du shader color
myProj.addValuedLink(myColor.getInVar('r'), 0.5)
myProj.addValuedLink(myColor.getInVar('g'), 1.0)
myProj.addValuedLink(myColor.getInVar('b'), 1.0)
myProj.addValuedLink(myColor.getInVar('a'), 1.0)

# assignation d'une valeur aux entrees du shader changeColor
myProj.addValuedLink(myChangeColor.getInVar('r'), 1.0)
myProj.addValuedLink(myChangeColor.getInVar('g'), 1.0)
myProj.addValuedLink(myChangeColor.getInVar('b'), 0.5)
myProj.addValuedLink(myChangeColor.getInVar('a'), 1.0)

# creation du lien entre color et change color
myProj.addLink(myColor.getOutVar('color'), myChangeColor.getInVar('color'))

# creation des liens d'entree/sortie du shader celShading
myProj.addLink(pixelInNormalVar, myCelShadingFragment.getInVar('normal'))
myProj.addLink(pixelInFragCoordVar, myFog.getInVar('fragCoord'))
myProj.addLink(myChangeColor.getOutVar('color'), myCelShadingFragment.getInVar('color'))

#creation des liens d'entree/sortie du shader fog
myProj.addLink(myCelShadingFragment.getOutVar('color'), myFog.getInVar('color'))
myProj.addLink(myFog.getOutVar('color'), pixelOutFinalColor)

# creation du lien entre pixel et vertex box
myProj.addLink(vertexOutNormalVar, pixelInNormalVar)


# sauvegarde du projet
myProj.save('test_save')

# creation d'un autre projet, et chargement du projet precedent
newProj = Project.Project.load('test_save')

# generation des shaders
newProj.compute('GLSLPrinter')

# rendu du resultat
newProj.render()
# newProj.render('model', [1, 1, 1], 0.2, 'weapon.obj')