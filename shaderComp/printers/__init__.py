##
# \authors Romain GUYOT de la HARDROUYERE
# \authors Matthieu BOURNAT
# \authors Antoine CHESNEAU
# \package shaderComp.printers
# \brief This package contains the class needed to print the code source of the shaders
# \version 0.1
# \date 2013-11-07
# \details In this module, a printer is implemented (as an inheriting class from `Printer`) for each platform supported by the library.
# \details The purpose of a printer is to run over the list of nodes of both boxes of the project, and to use for each node
# 	 the right generator to append the source code of the shader to the buffer that will be written in the resulting files
# \details By convention, it is assumed that for each shader and for each language, a generator can be found in this module
#  	in the folder that has the name of the shader. In this folder the generator is a class named `[ShaderName][PrinterName]`.
# \details For example, the generator of the shader `CelShading`, for the printer `GLSLPrinter` must be called `CelShadingGLSLPrinter`. 
__all__ = ["GLSLPrinter"]