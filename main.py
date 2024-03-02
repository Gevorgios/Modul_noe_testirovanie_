# import unittest
#
# class NumberSet:
#     def __init__(self, numbers):
#         self.numbers = numbers
#
#     def sum(self):
#         return sum(self.numbers)
#
#     def average(self):
#         return sum(self.numbers) / len(self.numbers)
#
#     def maximum(self):
#         return max(self.numbers)
#
#     def minimum(self):
#         return min(self.numbers)
#
#
# class TestNumberSet(unittest.TestCase):
#     def setUp(self):
#         self.numbers = [1, 2, 3, 4, 5]
#         self.num_set = NumberSet(self.numbers)
#
#     def test_sum(self):
#         self.assertEqual(self.num_set.sum(), 15)
#
#     def test_average(self):
#         self.assertEqual(self.num_set.average(), 3)
#
#     def test_maximum(self):
#         self.assertEqual(self.num_set.maximum(), 5)
#
#     def test_minimum(self):
#         self.assertEqual(self.num_set.minimum(), 1)
#
# if __name__ == '__main__':
#     unittest.main()


# 2


# import unittest
#
# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def set_value(self, new_value):
#         self.value = new_value
#
#     def get_value(self):
#         return self.value
#
#     def to_octal(self):
#         return oct(self.value)
#
#     def to_hexadecimal(self):
#         return hex(self.value)
#
#     def to_binary(self):
#         return bin(self.value)
#
#
# class TestNumber(unittest.TestCase):
#     def setUp(self):
#         self.num = Number(10)
#
#     def test_set_value(self):
#         self.num.set_value(20)
#         self.assertEqual(self.num.get_value(), 20)
#
#     def test_to_octal(self):
#         self.assertEqual(self.num.to_octal(), '0o12')
#
#     def test_to_hexadecimal(self):
#         self.assertEqual(self.num.to_hexadecimal(), '0xa')
#
#     def test_to_binary(self):
#         self.assertEqual(self.num.to_binary(), '0b1010')
#
# if __name__ == '__main__':
#     unittest.main()
