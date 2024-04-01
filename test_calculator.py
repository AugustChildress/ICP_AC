''''
import unittest
import calculator

class TestCalculatorAddition(unittest.TestCase):
    def setUp(self):
        pass
	
    def test_one_plus_one(self):
        expected = 2
        result = calculator.add(1,1)
        self.assertEqual(expected, result)

    def test_two_plus_two(self):
        expected = 4
        result = calculator.add(2,2)
        self.assertEqual(expected, result)
		
    def test_two_plus_negative_two(self):
        expected = 0
        result = calculator.add(2,-2)
        self.assertEqual(expected, result)

class TestCalculatorMultiplication(unittest.TestCase):
    def setUp(self):
        self.a = 2
        self.b = 4
    
    def test_two_times_four(self):
        expected = 8
        result = calculator.multiply(self.a, self.b)
        self.assertEqual(expected, result)
        
    def test_two_times_negative_four(self):
        expected = -8
        result = calculator.multiply(self.a, -self.b)
        self.assertEqual(expected, result)

class TestCalculatorDivision(unittest.TestCase):
    def test_divide_same_number(self):
        expected = 1
        result = calculator.divide(1,1)
        self.assertEqual(expected, result)

    def test_divide_different_number(self):
        expected = 0.5
        result = calculator.divide(1,2)
        self.assertEqual(expected, result)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(1,0)

    def test_tell_user_not_to_divide_by_zero(self):
        expected = "Don't divide by zero"
        result = calculator.divide(1,0)
        self.assertEqual(expected, result)

    def test_divide_different_number(self):
        expected = 0.5
        result = calculator.divide(1,2)
        self.assertEqual(expected, result)
        '''