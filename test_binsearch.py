import unittest

from binsearch import binary_search


import unittest

class MyTest(unittest.TestCase):


    def test_binsearch(self):
        input = list(range(10))
        self.assertEqual(binary_search(input, 5),5)
        self.assertEqual(binary_search(input, 4.5),-1)
        self.assertEqual(binary_search(input, 10),-1)
        self.assertEqual(binary_search([5], 5),0)

    def test_zerol(self):
        with self.assertRaises(ValueError):
            binary_search([],5)

    def test_nan(self):
        with self.assertRaises(TypeError):
            binary_search([1,float("nan"),4],5)

        
    # def test_char(self):
    #     with self.assertRaises(SyntaxError):
    #         binary_search([1,"blabla",4],5)
            



# WHEN DOING INCREMENTAL TEST

suite = unittest.TestLoader().loadTestsFromModule(MyTest())
unittest.TextTestRunner().run(suite)