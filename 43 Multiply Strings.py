"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also
represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Ex1:
Input: num1 = "2", num2 = "3"
Output: "6"

Ex2:
Input: num1 = "123", num2 = "456"
Output: "56088"
"""
import unittest


class Solution:
    def multiply(self, num1, num2):
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        for i in reversed(range(m)):
            carry = 0
            for j in reversed(range(n)):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                posLow = i + j + 1
                posHigh = i + j
                mul += result[posLow]
                result[posLow] = mul % 10
                result[posHigh] += mul // 10
        # e.g., num1='123', num2='456'; then result = [0, 5, 6, 0, 8, 8], res = [5, 6, 0, 8, 8]

        output = []
        for res in result:
            if len(output) != 0 or res != 0: # deal with leading zero issue
                output.append(res)
        return '0' if len(output) == 0 else ''.join(str(s) for s in output)

    def multiply1(self, num1: str, num2: str) -> str:
        res = 0
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                res += (ord(n1) - ord('0')) * (ord(n2) - ord('0')) * (10**(i+j))
        return str(res)


class testSolution(unittest.TestCase):
    def test0(self):
        num1 = '123'
        num2 = '456'
        output = '56088'
        self.assertEqual(Solution().multiply(num1, num2), output)
        self.assertEqual(Solution().multiply1(num1, num2), output)


if __name__ =='__main__':
    unittest.main()