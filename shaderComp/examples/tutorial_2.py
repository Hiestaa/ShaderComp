from shaderComp.core import *
from shaderComp.shaders import *
# notice the import of the shaders of the math module
from shaderComp.shaders.math import *

# creation of the project 'myFog'
myFogProject = Project.Project('tutorial_2')

# creation of the nodes
# remember that the first one is mandatory in the vertex box
myDefaultVertexShader = DefaultVertexShader.DefaultVertexShader()
myDispatchVect4 = DispatchVect4.DispatchVect4(ShaderType.PIXEL_SHADER)
myFloatDiv1 = FloatDiv.FloatDiv(ShaderType.PIXEL_SHADER)
myFloatDiv2 = FloatDiv.FloatDiv(ShaderType.PIXEL_SHADER)
myLog = Log.Log(ShaderType.PIXEL_SHADER)
myClamp = Clamp.Clamp(ShaderType.PIXEL_SHADER)
myMix = Mix.Mix(ShaderType.PIXEL_SHADER)

# adding nodes to the project
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

# creating input and output variables of the vertex box
vertexOutFinalPositionVar = myFogProject.addVertexOutVar('final_position', 'vec4')
vertexInVertVar = myFogProject.addVertexInVar('vertex', 'vec4')

# creating input and output variables of the pixel box
pixelInFragCoordVar = myFogProject.addPixelInVar('fragCoord', 'vec4')
pixelInColorVar = myFogProject.addPixelInVar('color', 'vec4')
pixelInFogFactorVar = myFogProject.addPixelInVar('fogFactor', 'float')
pixelInFogColorVar = myFogProject.addPixelInVar('fogColor', 'vec4')
pixelOutFinalColor = myFogProject.addPixelOutVar('color', 'vec4')

#creating links between the pipeline and the input of the boxes
myFogProject.addLink(myFogProject.getVertexPipelineVar('Vertex'), vertexInVertVar)
myFogProject.addLink(myFogProject.getPixelPipelineVar('FragCoord'), pixelInFragCoordVar)
myFogProject.addLink(myFogProject.getPixelPipelineVar('FogColor'), pixelInFogColorVar)

# creating links between the output of the boxes and the pipeline
myFogProject.addLink(vertexOutFinalPositionVar, myFogProject.getVertexPipelineVar('Position'))
myFogProject.addLink(pixelOutFinalColor, myFogProject.getPixelPipelineVar('FragColor'))

# creating links between input/output variables of the vertex box and the nodes it contains
myFogProject.addLink(vertexInVertVar, myDefaultVertexShader.getInVar('vertex'))
myFogProject.addLink(myDefaultVertexShader.getOutVar('position'), vertexOutFinalPositionVar)

# creating links between input/output variables of the pixel box and the nodes it contains
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

# adding valued link to the unlinked input variables of the pixel box
myFogProject.addValuedLink(pixelInColorVar, 'vec4(0.5, 0.5, 1.0, 1.0)')
myFogProject.addValuedLink(pixelInFogFactorVar, 25.0)

# computing using GLSL printer and rendering overview
myFogProject.compute('GLSLPrinter')
myFogProject.render()