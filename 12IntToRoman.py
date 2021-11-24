import unittest

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Ex1: 2    -->   II

Ex2: 12   -->   XII

Ex3: 27   -->   XXVII

"""


class solution0:
    def intToRoman(self, num: int) -> str:
        dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L',
               40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        out = ''
        for i in dic:
            out += (num // i) * dic[i]
            num = num % i

        return out


class solution1:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        out = ''
        for i, s_ in zip(values, numerals):
            out += (num // i) * s_
            num %= i
        return out


class TestSolution0(unittest.TestCase):
    def test0(self):
        num = 123
        output = 'CXXIII'
        self.assertEqual(solution0().intToRoman(num), output)

    def test1(self):
        num = 1994
        output = 'MCMXCIV'
        self.assertEqual(solution0().intToRoman(num), output)

    def test2(self):
        num = 58
        output = 'LVIII'
        self.assertEqual(solution0().intToRoman(num), output)

    def test4(self):
        num = 9
        output = 'IX'
        self.assertEqual(solution0().intToRoman(num), output)


class TestSolution1(unittest.TestCase):
    def test0(self):
        num = 123
        output = 'CXXIII'
        self.assertEqual(solution1().intToRoman(num), output)

    def test1(self):
        num = 1994
        output = 'MCMXCIV'
        self.assertEqual(solution1().intToRoman(num), output)

    def test2(self):
        num = 58
        output = 'LVIII'
        self.assertEqual(solution1().intToRoman(num), output)

    def test4(self):
        num = 9
        output = 'IX'
        self.assertEqual(solution0().intToRoman(num), output)


if __name__ == "__main__":
    unittest.main()