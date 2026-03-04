import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.myCalc = Calculator(8,2)

    def test_sum(self):
        self.assertEqual(self.myCalc.get_sum(), 10, "The answer is not 4!")

    def test_subtraction(self):
        self.assertEqual(self.myCalc.get_subtraction(), 6, "The difference is wrong!")
    
    def test_multiplication(self):
        self.assertEqual(self.myCalc.get_multiplication(),16, "The product is wrong!")

    def test_division(self):
        self.assertEqual(self.myCalc.get_division(),4, "the division is wrong!")


if __name__ == "__main__":

    unittest.main()