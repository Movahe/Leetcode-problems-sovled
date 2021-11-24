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

"""


class solution0:
    def romanToInt(self, s)->int:
        result = 0
        roman_dict = {"I": 1,
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000,
                      }

        s = list(s)

        while len(s) > 0:
            cur = s.pop(0)
            if len(s) > 0 and roman_dict[s[0]] > roman_dict[cur]:
                result += roman_dict[s[0]] - roman_dict[cur]
                s.pop(0)

            else:
                result += roman_dict[cur]
        return result


class solution1:
    def romanToInt(self, s):
        roman_dict = {'M': 1000,
                      'D': 500,
                      'C': 100,
                      'L': 50,
                      'X': 10,
                      'V': 5,
                      'I': 1,
                      }
        res = 0
        for i in range(len(s) - 1):
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                res -= roman_dict[s[i]]
            else:
                res += roman_dict[s[i]]
        return res + roman_dict[s[-1]]


class Testsolution0(unittest.TestCase):
    def test0(self):
        s1 = "III"   #->3
        s2 = "IV"    #->4
        s3 = "IX"    #->9
        s4 = "LVIII" #->58
        s5 = "MCMXCIV"  #==>1994
        self.assertEqual(solution0().romanToInt(s1), 3)
        self.assertEqual(solution0().romanToInt(s2), 4)
        self.assertEqual(solution0().romanToInt(s3), 9)
        self.assertEqual(solution0().romanToInt(s4), 58)
        self.assertEqual(solution0().romanToInt(s5), 1994)


class Testsolution1(unittest.TestCase):
    def test0(self):
        s1 = "III"   #->3
        s2 = "IV"    #->4
        s3 = "IX"    #->9
        s4 = "LVIII" #->58
        s5 = "MCMXCIV"  #==>1994
        self.assertEqual(solution1().romanToInt(s1), 3)
        self.assertEqual(solution1().romanToInt(s2), 4)
        self.assertEqual(solution1().romanToInt(s3), 9)
        self.assertEqual(solution1().romanToInt(s4), 58)


if __name__ == "__main__":
    unittest.main()
