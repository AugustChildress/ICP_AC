import unittest
import my_program as my_program

class TestMyProgram(unittest.TestCase):
    def test_one_plus_one(self):
        expected = 2
        result = my_program.add(1,1)
        self.assertEqual(expected, result)
    