# This file is used to load the Tests altogether.
import unittest
from tests.home.expedia_testing import TestingLogin
from tests.home.expediatesting2 import Optionstesting
from tests.home.expediatesting3 import StaysTesting

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestingLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Optionstesting)
tc3 = unittest.TestLoader().loadTestsFromTestCase(StaysTesting)

smoketest = unittest.TestSuite([tc1,tc2,tc3]) #([tc1,tc2,tc3])

unittest.TextTestRunner(verbosity=2).run(smoketest)