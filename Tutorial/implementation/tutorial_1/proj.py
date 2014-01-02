from shaderComp.core import *
from shaderComp.shaders import *

myProj = Project.Project('firstProject')

myColor = Color.Color()
myDefaultVertexShader = DefaultVertexShader.DefaultVertexShader()


myProj.appendNode(myColor)
myProj.appendNode(myDefaultVertexShader)

myColor.setParams(0, 0.3, 0.6, 1.0);

vertexInVertVar = myProj.addVertexInVar('vertex', 'vec4')
vertexOutFinalPositionVar = myProj.addVertexOutVar('final_position', 'vec4')
pixelOutFinalColor = myProj.addPixelOutVar('final_color', 'vec4')

myProj.addLink(vertexInVertVar, myDefaultVertexShader.getInVar('vertex'))
myProj.addLink(myDefaultVertexShader.getOutVar('position'), vertexOutFinalPositionVar)
myProj.addLink(myColor.getOutVar('color'), pixelOutFinalColor)

myProj.addLink(myProj.getVertexPipelineVar('Vertex'), vertexInVertVar)
myProj.addLink(vertexOutFinalPositionVar, myProj.getVertexPipelineVar('Position'))
myProj.addLink(pixelOutFinalColor, myProj.getPixelPipelineVar('FragColor'))

myProj.compute('GLSLPrinter');
myProj.render();