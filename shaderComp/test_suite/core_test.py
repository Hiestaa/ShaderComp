##
# @authors Romain GUYOT de la HARDROUYERE
# @authors Matthieu BOURNAT
# @authors Antoine CHESNEAU
# @package shaderComp.test_suite.core_test
# @brief This package provides interface with all the unit tests of the test suite
# @version 1.0
# @date 2014-01-07
# @details to run the test suite from the command line, change current directory to the parent of shaderComp folder and type:
# python -m shaderComp.test_suite.core_test [--help: list of available options]

from test_project import *
from test_test import *

import unittest

def run():
    unittest.main()

if __name__ == '__main__':
    run()