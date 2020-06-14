import unittest
import katas
class TestKatas(unittest.TestCase):\
    
    def test_add(self):
        self.assertEqual((7 + 5), 12)
    def test_multiply(self):
        self.assertEqual((9 * 8), 72)
    def test_power(self):
        self.assertTrue((5, 5), 3125)
    def test_factorial(self):
        self.assertTrue(8, 40320)
    def test_fibonacci(self):
        self.assertTrue((3,5), 8)
        

if __name__ == '__main__':
    unittest.main()
