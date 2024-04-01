import unittest #I can import the unittest package
import ICPCH7 #I can import a module that I have written into my test module

class TestICPCH7(unittest.TestCase):
    def setUp(self):
        pass
	
    def test_one_plus_one(self):
        expected = 2
        result = ICPCH7.add(1,1)
        self.assertEqual(expected, result) #I can write a unit test using assertEqual
    
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            ICPCH7.divide(1,0)#I can write a unit test using assertRaises

    def test_equal(self):
        self.assertTrue(ICPCH7.equal(2,2)) #I can write a unit test using assertTrue or assertFalse

    def test_almost_equal(self):# I can write a unit test using assertAlmostEqual 
        expected = 0.3333333
        result = ICPCH7.divide(1,3)
        self.assertAlmostEqual(expected, result, places = 4)

    