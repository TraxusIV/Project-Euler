from ProjectEuler import *
from unittest import *

class TestEuler1(object):
    """docstring for TestEuler1"""
    def TestQuestion(self):
        testcase1 = Euler1(1000)
        assertEqual(33, testcase1.solve())
        
TestEuler1.TestQuestion()