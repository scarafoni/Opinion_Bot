'''
Created on Jul 13, 2014

@author: dan_Fedora
'''
import unittest
class opinion_bot_test(unittest.TestCase):
    def test_add(self):
        x= 1
        y = 2
        z = x+y
        self.assertEqual(z, 3, "math broken")