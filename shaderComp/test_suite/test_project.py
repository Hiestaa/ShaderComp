##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.test_suite.test_project
# @brief This module provides unit testing of the class Project
# @version 1.0
# @date 2014-01-07

import unittest

from ..core import *
from ..shaders.math import *
from ..shaders import *
from ..core import ShaderType

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class TestProjectCreation
# @brief This class provides unit tests related to the creation of a new empty project
# @version 1.0
# @date 2014-01-07
class TestProjectCreation(unittest.TestCase):

    def setUp(self):
        self.project = Project.Project('project_tester')

    def test_init(self):
        self.assertIsNotNone(self.project,
            "Project's linkManager is None.")
        self.assertEqual("project_tester", self.project.name,
            "Project is not correctly named.")
        self.assertIsNotNone(self.project.linkManager,
            "Project's linkManager is None.")
        self.assertIsNotNone(self.project.pixelBox,
            "Project's pixelBox is None.")
        self.assertIsNotNone(self.project.vertexBox,
            "Project's vertexBox is None.")

    def test_getters(self):
        self.assertEqual(self.project.getVertexBox(), self.project.vertexBox,
            "Getter getVertexBox does not return expected datas")
        self.assertEqual(self.project.getPixelBox(), self.project.pixelBox,
            "Getter getPixelBox does not return expected datas")
        self.assertEqual(self.project.getBox("vertex"), self.project.vertexBox,
            "Getter getBox does not return expected datas")
        self.assertEqual(self.project.getBox("pixel"), self.project.pixelBox,
            "Getter getBox does not return expected datas")


##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class TestProjectLinking
# @brief This class provides unit tests related to the edition of the links inside a project
# @version 1.0
# @date 2014-01-07
class TestProjectLinking(unittest.TestCase):

    def setUp(self):
        self.project = Project.Project('project_tester')
        myClamp = Clamp.Clamp(ShaderType.PIXEL_SHADER)
        self.myClamp = myClamp
        myDefaultVertexShader = DefaultVertexShader.DefaultVertexShader()
        self.myDefaultVertexShader = myDefaultVertexShader
        self.project.appendNode(myClamp)
        self.project.appendNode(myDefaultVertexShader)
        self.project.addValuedLink(myClamp.getInVar('min'), 0.0)
        self.project.addValuedLinkNode(myClamp, myClamp.getInVar('max'), 1.0)
        self.project.addValuedLinkByName(myDefaultVertexShader, 'vertex', 1.0)

    def test_getLinkList(self):
        self.assertEqual(len(self.project.getLinkList("vertex")), 1,
            "Getter getLinkList does not return the right list for vertexBox")
        self.assertEqual(len(self.project.getLinkList("pixel")), 2,
            "Getter getLinkList does not return the right list for pixelBox")

    def test_addLink(self):
        myLog = Log.Log(ShaderType.PIXEL_SHADER)
        self.project.appendNode(myLog)
        self.assertFalse(self.project.linkManager.containLinkTo(myLog, myLog.getInVar('input')),
            "Link already present")
        self.project.addLink(self.myClamp.getOutVar('result'), myLog.getInVar('input'))
        self.assertTrue(self.project.linkManager.containLinkTo(myLog, myLog.getInVar('input')),
            "Link has not been added")

    def test_addLinkNode(self):
        myLog = Log.Log(ShaderType.PIXEL_SHADER)
        self.project.appendNode(myLog)
        self.assertFalse(self.project.linkManager.containLinkTo(myLog, myLog.getInVar('input')),
            "Link already present")
        self.project.addLinkNode(self.myClamp, self.myClamp.getOutVar('result'), myLog, myLog.getInVar('input'))
        self.assertTrue(self.project.linkManager.containLinkTo(myLog, myLog.getInVar('input')),
            "Link has not been added")

    def test_addValuedLink(self):
        self.assertTrue(self.project.linkManager.containLinkTo(self.myClamp, self.myClamp.getInVar('min')),
            "Valued Link has not been added")
        self.assertTrue(self.project.linkManager.containLinkTo(self.myClamp, self.myClamp.getInVar('max')),
            "Valued Link has not been added")
        self.assertTrue(self.project.linkManager.containLinkTo(self.myDefaultVertexShader, self.myDefaultVertexShader.getInVar('vertex')),
            "Valued Link has not been added")

    def test_deleteLink(self):
        myLog = Log.Log(ShaderType.PIXEL_SHADER)
        self.project.appendNode(myLog)
        self.project.addLink(self.myClamp.getOutVar('result'), myLog.getInVar('input'))
        self.assertTrue(self.project.linkManager.containLinkTo(myLog, myLog.getInVar('input')),
            "Link has not been added")
        self.project.deleteLink(self.myClamp, myLog, self.myClamp.getOutVar('result'), myLog.getInVar('input'))
        self.assertFalse(self.project.linkManager.containLinkTo(myLog, myLog.getInVar('input')),
            "Link has not been deleted")
        self.project.addValuedLink(myLog.getInVar('input'), 0.0)
        self.assertTrue(self.project.linkManager.containLinkTo(myLog, myLog.getInVar('input')),
            "Link has not been added")
        self.project.deleteValuedLink(myLog, myLog.getInVar('input'))
        self.assertFalse(self.project.linkManager.containLinkTo(myLog, myLog.getInVar('input')),
            "Link has not been deleted")



##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class TestProjectNodeEdition
# @brief This class provides unit tests related to the the edition of the node a project is holding
# @version 1.0
# @date 2014-01-07
class TestProjectNodeEdition(unittest.TestCase):

    def setUp(self):
        self.project = Project.Project('project_tester')
        myClamp = Clamp.Clamp(ShaderType.PIXEL_SHADER)
        self.myClamp = myClamp
        myDefaultVertexShader = DefaultVertexShader.DefaultVertexShader()
        self.project.appendNode(myClamp)
        self.project.appendNode(myDefaultVertexShader)
        self.project.addValuedLink(myClamp.getInVar('min'), 0.0)
        self.project.addValuedLink(myClamp.getInVar('max'), 1.0)
        self.project.addValuedLink(myDefaultVertexShader.getInVar('vertex'), 1.0)

    def test_clearBox(self):
        self.project.clearBox('vertex')
        self.assertEqual(len(self.project.vertexBox.nodeList), 0,
            "clearBox on 'vertex' does not clear the vertexBox")
        self.project.clearBox('pixel')
        self.assertEqual(len(self.project.pixelBox.nodeList), 0,
            "clearBox on 'pixel' does not clear the pixelBox")

    def test_clearBoxAll(self):
        self.project.clearBox('all')
        self.assertEqual(len(self.project.vertexBox.nodeList), 0,
            "clearBox on 'all' does not clear the vertexBox")
        self.assertEqual(len(self.project.pixelBox.nodeList), 0,
            "clearBox on 'all' does not clear the pixelBox")

    def test_clear(self):
        self.project.clear()
        self.assertEqual(len(self.project.vertexBox.nodeList), 0,
            "clear does not clear the vertexBox")
        self.assertEqual(len(self.project.pixelBox.nodeList), 0,
            "clear does not clear the pixelBox")

    def test_addNode(self):
        myLog = Log.Log(ShaderType.PIXEL_SHADER)
        self.project.addNode(myLog, 0)
        self.assertIn(myLog, self.project.pixelBox.nodeList,
            "Added node is not in the node list of the box it belongs to")
        self.assertEqual(myLog, self.project.pixelBox.nodeList[0],
            "Added node is not at the epected position of the node list")

    def test_appendNode(self):
        myLog = Log.Log(ShaderType.PIXEL_SHADER)
        self.project.appendNode(myLog)
        self.assertIn(myLog, self.project.pixelBox.nodeList,
            "Appended node is not in the node list of the box it belongs to")

    def test_removeNode(self):
        myLog = Log.Log(ShaderType.PIXEL_SHADER)
        self.project.appendNode(myLog)
        self.project.removeNode(myLog)
        self.assertNotIn(myLog, self.project.pixelBox.nodeList,
            "Removed node is still in the node list of the box it belongs to")

    def test_removeNode2(self):
        self.project.removeNode(self.myClamp)
        self.assertNotIn(self.myClamp, self.project.pixelBox.nodeList,
            "Removed node is still in the node list of the box it belongs to")

    def test_removeNodeAt(self):
        myLog = Log.Log(ShaderType.PIXEL_SHADER)
        self.project.addNode(myLog, 0)
        self.project.removeNodeAt(0, 'pixel')
        self.assertNotIn(myLog, self.project.pixelBox.nodeList,
            "Removed node is still in the node list of the pixel box")
        myLog = Log.Log(ShaderType.VERTEX_SHADER)
        self.project.addNode(myLog, 0)
        self.project.removeNodeAt(0, 'vertex')
        self.assertNotIn(myLog, self.project.vertexBox.nodeList,
            "Removed node is still in the node list of the vertex box")

    def test_addVertexBoxVar(self):
        test_input_v = self.project.addVertexInVar('test_input_v', 'float')
        self.assertIsNotNone(test_input_v,
            "addVertexInVar does not return the required reference")
        self.assertEqual(test_input_v.name, 'test_input_v',
            "The added variable did does not have the right name")
        self.assertEqual(test_input_v.type, 'float',
            "The added variable did does not have the right type")
        self.assertEqual(test_input_v.varType, Var.VarType.IN,
            "The added variable did does not have the right varType (IN)")
        self.assertEqual(test_input_v, self.project.vertexBox.inVars['test_input_v'])
        self.assertEqual(test_input_v, self.project.getVertexInVar('test_input_v'))
        test_output_v = self.project.addVertexOutVar('test_output_v', 'float')
        self.assertIsNotNone(test_output_v,
            "addVertexOutVar does not return the required reference")
        self.assertEqual(test_output_v.name, 'test_output_v',
            "The added variable did does not have the right name")
        self.assertEqual(test_output_v.type, 'float',
            "The added variable did does not have the right type")
        self.assertEqual(test_output_v.varType, Var.VarType.OUT,
            "The added variable did does not have the right varType (OUT)")
        self.assertEqual(test_output_v, self.project.vertexBox.outVars['test_output_v'])
        self.assertEqual(test_output_v, self.project.getVertexOutVar('test_output_v'))
        test_uniform_v = self.project.addVertexUniform('test_uniform_v', 'test_uniform_v', 'float')
        self.assertIsNotNone(test_uniform_v,
            "addVertexUniform does not return the required reference")
        self.assertEqual(test_uniform_v.name, 'test_uniform_v',
            "The added variable did does not have the right name")
        self.assertEqual(test_uniform_v.type, 'float',
            "The added variable did does not have the right type")
        self.assertEqual(test_uniform_v.varType, Var.VarType.UNI,
            "The added variable did does not have the right varType (UNI)")
        self.assertEqual(test_uniform_v.val, 'test_uniform_v',
            "The added variable did does not have the right varType (UNI)")
        self.assertEqual(test_uniform_v, self.project.vertexBox.uniforms['test_uniform_v'])
        self.assertEqual(test_uniform_v, self.project.getVertexUniform('test_uniform_v'))


    def test_addPixelBoxVar(self):
        test_input_p = self.project.addPixelInVar('test_input_p', 'float')
        self.assertIsNotNone(test_input_p,
            "addPixelInVar does not return the required reference")
        self.assertEqual(test_input_p.name, 'test_input_p',
            "The added variable did does not have the right name")
        self.assertEqual(test_input_p.type, 'float',
            "The added variable did does not have the right type")
        self.assertEqual(test_input_p.varType, Var.VarType.IN,
            "The added variable did does not have the right varType (IN)")
        self.assertEqual(test_input_p, self.project.pixelBox.inVars['test_input_p'])
        self.assertEqual(test_input_p, self.project.getPixelInVar('test_input_p'))
        test_output_p = self.project.addPixelOutVar('test_output_p', 'float')
        self.assertIsNotNone(test_output_p,
            "addPixelOutVar does not return the required reference")
        self.assertEqual(test_output_p.name, 'test_output_p',
            "The added variable did does not have the right name")
        self.assertEqual(test_output_p.type, 'float',
            "The added variable did does not have the right type")
        self.assertEqual(test_output_p.varType, Var.VarType.OUT,
            "The added variable did does not have the right varType (OUT)")
        self.assertEqual(test_output_p, self.project.pixelBox.outVars['test_output_p'])
        self.assertEqual(test_output_p, self.project.getPixelOutVar('test_output_p'))
        test_uniform_p = self.project.addPixelUniform('test_uniform_p', 'test_uniform_p', 'float')
        self.assertIsNotNone(test_uniform_p,
            "addPixelUniform does not return the required reference")
        self.assertEqual(test_uniform_p.name, 'test_uniform_p',
            "The added variable did does not have the right name")
        self.assertEqual(test_uniform_p.type, 'float',
            "The added variable did does not have the right type")
        self.assertEqual(test_uniform_p.varType, Var.VarType.UNI,
            "The added variable did does not have the right varType (UNI)")
        self.assertEqual(test_uniform_p.val, 'test_uniform_p',
            "The added variable did does not have the right varType (UNI)")
        self.assertEqual(test_uniform_p, self.project.pixelBox.uniforms['test_uniform_p'])
        self.assertEqual(test_uniform_p, self.project.getPixelUniform('test_uniform_p'))

    def test_pipelineVar(self):
        self.assertIsNotNone(self.project.getVertexPipelineVar('Vertex'),
            "The 'Vertex' variable does not exists in the vertex pipeline")
        self.assertIsNotNone(self.project.getVertexPipelineVar('Normal'),
            "The 'Normal' variable does not exists in the vertex pipeline")
        self.assertIsNotNone(self.project.getVertexPipelineVar('Position'),
            "The 'Position' variable does not exists in the vertex pipeline")
        self.assertIsNotNone(self.project.getVertexPipelineVar('Color'),
            "The 'Color' variable does not exists in the vertex pipeline")
        self.assertIsNotNone(self.project.getVertexPipelineVar('FragColor'),
            "The 'FragColor' variable does not exists in the vertex pipeline")
        self.assertIsNotNone(self.project.getVertexPipelineVar('FragCoord'),
            "The 'FragCoord' variable does not exists in the vertex pipeline")
        self.assertIsNotNone(self.project.getVertexPipelineVar('FogColor'),
            "The 'FogColor' variable does not exists in the vertex pipeline")
        self.assertIsNotNone(self.project.getPixelPipelineVar('Vertex'),
            "The 'Vertex' variable does not exists in the pixel pipeline")
        self.assertIsNotNone(self.project.getPixelPipelineVar('Normal'),
            "The 'Normal' variable does not exists in the pixel pipeline")
        self.assertIsNotNone(self.project.getPixelPipelineVar('Position'),
            "The 'Position' variable does not exists in the pixel pipeline")
        self.assertIsNotNone(self.project.getPixelPipelineVar('Color'),
            "The 'Color' variable does not exists in the pixel pipeline")
        self.assertIsNotNone(self.project.getPixelPipelineVar('FragColor'),
            "The 'FragColor' variable does not exists in the pixel pipeline")
        self.assertIsNotNone(self.project.getPixelPipelineVar('FragCoord'),
            "The 'FragCoord' variable does not exists in the pixel pipeline")
        self.assertIsNotNone(self.project.getPixelPipelineVar('FogColor'),
            "The 'FogColor' variable does not exists in the pixel pipeline")

##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @class TestProjectManagement
# @brief This class provides unit tests related to the saving/loading of the project and the box of this project
# @version 1.0
# @date 2014-01-07
class TestProjectManagement(unittest.TestCase):

    def setUp(self):
        self.project = Project.Project('test_project')
        myColor = Color.Color()
        self.myColor = myColor
        myDefaultVertexShader = DefaultVertexShader.DefaultVertexShader()
        self.myDefaultVertexShader = myDefaultVertexShader

        self.project.appendNode(myColor)
        self.project.appendNode(myDefaultVertexShader)
        myColor.setParams(0, 0.3, 0.6, 1.0);
        vertexInVertVar = self.project.addVertexInVar('vertex', 'vec4')
        vertexOutFinalPositionVar = self.project.addVertexOutVar('final_position', 'vec4')
        pixelOutFinalColor = self.project.addPixelOutVar('final_color', 'vec4')

        self.project.addLink(vertexInVertVar, myDefaultVertexShader.getInVar('vertex'))
        self.project.addLink(myDefaultVertexShader.getOutVar('position'), vertexOutFinalPositionVar)
        self.project.addLink(myColor.getOutVar('color'), pixelOutFinalColor)
        self.project.addLink(self.project.getVertexPipelineVar('Vertex'), vertexInVertVar)
        self.project.addLink(vertexOutFinalPositionVar, self.project.getVertexPipelineVar('Position'))
        self.project.addLink(pixelOutFinalColor, self.project.getPixelPipelineVar('FragColor'))

    def test_compute(self):
        import os.path

        self.project.compute('GLSLPrinter')

        self.assertTrue(os.path.exists('test_project'))
        self.assertTrue(os.path.exists('test_project/vertexShader.glsl'))
        self.assertTrue(os.path.exists('test_project/fragmentShader.glsl'))

        import shutil
        shutil.rmtree('test_project')


    def test_save(self):
        import os.path
        self.project.save('test_project_sav.bin')
        self.assertTrue(os.path.exists('test_project_sav.bin'))
        os.remove('test_project_sav.bin')

    def test_load(self):
        import os.path
        self.project.save('test_project_sav.bin')
        self.assertTrue(os.path.exists('test_project_sav.bin'))
        newproj = Project.Project.load('test_project_sav.bin')
        newproj.compute('GLSLPrinter')
        os.remove('test_project_sav.bin')


        self.assertTrue(os.path.exists('test_project'))
        self.assertTrue(os.path.exists('test_project/vertexShader.glsl'))
        self.assertTrue(os.path.exists('test_project/fragmentShader.glsl'))

        import shutil
        shutil.rmtree('test_project')

    def test_save_box(self):
        import os.path
        self.project.saveBox('test_project_pixel_box.bin', 'pixel')
        self.project.saveBox('test_project_vertex_box.bin', 'vertex')
        self.assertTrue(os.path.exists('test_project_pixel_box.bin'))
        self.assertTrue(os.path.exists('test_project_vertex_box.bin'))

        os.remove('test_project_pixel_box.bin')
        os.remove('test_project_vertex_box.bin')

    def test_load_box(self):
        import os.path
        self.project.saveBox('test_project_pixel_box.bin', 'pixel')
        self.project.saveBox('test_project_vertex_box.bin', 'vertex')

        newProj = Project.Project('load_box_test')
        newProj.loadBox('test_project_pixel_box.bin', 'pixel')
        newProj.loadBox('test_project_vertex_box.bin', 'vertex')

        self.assertEqual(newProj.pixelBox.name, 'Pixeltest_project')
        self.assertEqual(newProj.vertexBox.name, 'Vertextest_project')
        self.assertEqual(self.myColor.name, newProj.pixelBox.nodeList[0].name,
            "The added node is not present in the loaded pixel box")
        self.assertEqual(self.myDefaultVertexShader.name, newProj.vertexBox.nodeList[0].name,
            "The added node is not present in the loaded vertex box")

        newProj.appendNode(newProj.loadBoxAsNode('test_project_pixel_box.bin'))
        self.assertEqual(newProj.pixelBox.nodeList[1].name, 'Pixeltest_project',
            "When loading box as node, the loaded node has corrupted member fields value")

        os.remove('test_project_pixel_box.bin')
        os.remove('test_project_vertex_box.bin')