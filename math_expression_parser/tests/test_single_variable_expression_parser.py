import unittest
from ..single_variable_parser import SingleVariableParser

class TestSingleVariableParser(unittest.TestCase):
    
    def test_simple_constants_expressions(self):
        parser = SingleVariableParser()
        parser.set_math_function_text('1+1')
        self.assertEqual(parser.compute_function_at_value(0), 2)
    
    def test_complex_constants_expressions(self):
        parser = SingleVariableParser()
        parser.set_math_function_text('sqr((18sub3)/3*(2+3))^2')
        self.assertEqual(parser.compute_function_at_value(0), 25)

if __name__ == '__main__':
    unittest.main()