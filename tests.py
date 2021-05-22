import unittest
from task import conv_endian
from task import conv_num
import random


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test2_function3(self):
        """tests for correct conversion of decimal to hex in both negative and positive random decimal numbers
        for big endian"""
        num_tests = 1000
        for i in range(num_tests):
            negative = False
            num = random.randint(-9223372036854775807, 9223372036854775807)

            # changes negative values to positive for conversion and sets flag for negative value
            if num < 0:
                negative = True
                num = abs(num)
            correct_hex = str(hex(num))         # converts decimal to string hex with built-in
            correct_hex = correct_hex[2:]      # takes off the "0x" from front of hex

            # formats hex str: adds spacing to hex (every 2 chars) & adds 0 to front if length is odd.
            if len(correct_hex) % 2 != 0:
                space = 1
                format_hex = '0'
            else:
                space = 0
                format_hex = ''
            for char in correct_hex:
                format_hex = format_hex + char
                space += 1
                if space == 2:
                    format_hex = format_hex + ' '
                    space = 0
            format_hex = format_hex[:-1]

            # converts back to negative value if negative variable is True
            if negative is True:
                format_hex = '-' + format_hex
            if negative is True:
                num = num * -1

            my_hex = conv_endian(num, endian='big')
            message = "test failed for num " + str(num)
            self.assertEqual(format_hex.upper(), my_hex, message)

    def test1_function1(self):
        msg = "Test failed for empty string"
        self.assertIsNone(conv_num(''), msg)

    def test2_function1(self):
        num_str = "12345A"
        msg = "Test failed for " + num_str
        self.assertIsNone(conv_num(num_str), msg)

    def test3_function1(self):
        num_str = "12.3.45"
        msg = "Test failed for " + num_str
        self.assertIsNone(conv_num(num_str), msg)

    def test4_function1(self):
        num_str = "0"
        msg = "Test failed for " + num_str
        self.assertEqual(float(num_str), conv_num(num_str), msg)

    def test5_function1(self):
        num_str = "12345"
        msg = "Test failed for " + num_str
        self.assertEqual(float(num_str), conv_num(num_str), msg)

    def test6_function1(self):
        num_str = "-123.45"
        msg = "Test failed for " + num_str
        self.assertEqual(float(num_str), conv_num(num_str), msg)

    def test7_function1(self):
        num_str = ".45"
        msg = "Test failed for " + num_str
        self.assertEqual(float(num_str), conv_num(num_str), msg)

    def test8_function1(self):
        num_str = "123."
        msg = "Test failed for " + num_str
        self.assertEqual(float(num_str), conv_num(num_str), msg)

    def test9_function1(self):
        num_str = "0xAZ4"
        msg = "Test failed for " + num_str
        self.assertIsNone(conv_num(num_str), msg)

    def test10_function1(self):
        num_str = "0xAD4"
        msg = "Test failed for " + num_str
        self.assertEqual(2772, conv_num(num_str), msg)

    def test11_function1(self):
        num_str = "-0xAD4"
        msg = "Test failed for " + num_str
        self.assertEqual(-2772, conv_num(num_str), msg)

    def test12_function1(self):
        num_str = "0x0"
        msg = "Test failed for " + num_str
        self.assertEqual(0, conv_num(num_str), msg)


if __name__ == '__main__':
    unittest.main()
