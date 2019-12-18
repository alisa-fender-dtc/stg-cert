from fibonacci import get_fibonacci_number_from_order as get_fib
from number_stringify import stringify
import unittest


class Challenge4(unittest.TestCase):
    def test_fibonacci(self):
        test_orders = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 25, 42, 100 ]
        for test_order in test_orders:
            fibonacci_number = get_fib(test_order)
            print("The Fibonacci number at position {} is {}.".format(test_order, fibonacci_number))
            print("Strigified: " + stringify(fibonacci_number))


if __name__ == '__main__':
    unittest.main()
