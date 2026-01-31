import unittest
from src import calculator  # Import your calculator module

class TestCalculator(unittest.TestCase):

    # Test for fun1 (addition)
    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)  # 2 + 3 = 5
        self.assertEqual(calculator.fun1(5, 0), 5)  # 5 + 0 = 5
        self.assertEqual(calculator.fun1(-1, 1), 0)  # -1 + 1 = 0
        self.assertEqual(calculator.fun1(-1, -1), -2)  # -1 + -1 = -2

    # Test for fun2 (subtraction)
    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)  # 2 - 3 = -1
        self.assertEqual(calculator.fun2(5, 0), 5)  # 5 - 0 = 5
        self.assertEqual(calculator.fun2(-1, 1), -2)  # -1 - 1 = -2
        self.assertEqual(calculator.fun2(-1, -1), 0)  # -1 - -1 = 0

    # Test for fun3 (multiplication)
    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)  # 2 * 3 = 6
        self.assertEqual(calculator.fun3(5, 0), 0)  # 5 * 0 = 0
        self.assertEqual(calculator.fun3(-1, 1), -1)  # -1 * 1 = -1
        self.assertEqual(calculator.fun3(-1, -1), 1)  # -1 * -1 = 1

    # Test for fun4 (sum of three numbers)
    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)  # 2 + 3 + 5 = 10
        self.assertEqual(calculator.fun4(5, 0, -1), 4)  # 5 + 0 + -1 = 4
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)  # -1 + -1 + -1 = -3
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)  # -1 + -1 + 100 = 98

# This runs the test cases when the script is executed
if __name__ == '__main__':
    unittest.main()

