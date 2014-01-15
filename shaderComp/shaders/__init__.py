##
# \authors Romain GUYOT de la HARDROUYERE
# \authors Matthieu BOURNAT
# \authors Antoine CHESNEAU
# \package shaderComp.shaders
# \brief This package contains all the shaders that you can add as a node to a project
# \version 0.1
# \date 2013-11-07
# \details Each shader class has a set of input variables and output variable.
# \details The input variables can be set to a specified value with a `ValuedLink` (see `core.ValuedLink`)
#  they can be used to link this shader input to the output of another one or to
#  a readable item of the pipeline.
# \details The output variables can as well be linked to the input of another shader or to a writable item of the pipeline.
# \details With the use of the input variables and output variables of each shader of a project,
#  a graph can be build to link to input pipeline to the output pipeline
# \see first_project_example.py
# \see shader_link_example.py
# \example shader_link_example.py
__all__ = ["CelShadingFragment", "CelShadingVertex", "ChangeColor", "Color", "DefaultVertexShader","Fog", "VertexTestShader", "FragmenTestShader"]