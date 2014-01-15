##
# \authors Romain GUYOT de la HARDROUYERE
# \authors Matthieu BOURNAT
# \authors Antoine CHESNEAU
# \package shaderComp.test_suite
# \brief This package contains the needed files to run the test suite.
# \version 1.0
# \date 2014-01-07
# \details The test suite can be run using the following command: `python -m shaderComp.test_suite.test',
# from the parent folder of shaderComp in the command line.
# If all the test pass, nothing is displayed. Add the `-v' argument to get some more informations.
# If any of the test fails, the output will be displayed to you at the end of the checks.
# The total number of fails/errors will be printed at the end of the log.
__all__ = ["core_test", "test_project"]