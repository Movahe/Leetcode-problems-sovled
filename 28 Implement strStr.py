"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
and Java's indexOf().

Ex1:

Input: haystack = "hello", needle = "ll"
Output: 2
"""
import unittest


class solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1

    def strStr1(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    def strStr2(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        return haystack.index(needle)


class testSolutions(unittest.TestCase):
    def test0(self):
        haystack = "hello"
        needle = "ll"
        out = 2
        self.assertEqual(solution().strStr(haystack, needle), out)
        self.assertEqual(solution().strStr1(haystack, needle), out)
        self.assertEqual(solution().strStr2(haystack, needle), out)

    def test1(self):
        haystack = "aaaaa"
        needle = "baa"
        out = -1
        self.assertEqual(solution().strStr(haystack, needle), out)
        self.assertEqual(solution().strStr1(haystack, needle), out)
        self.assertEqual(solution().strStr2(haystack, needle), out)

    def test2(self):
        haystack = ""
        needle = ""
        out = 0
        self.assertEqual(solution().strStr(haystack, needle), out)
        self.assertEqual(solution().strStr1(haystack, needle), out)
        self.assertEqual(solution().strStr2(haystack, needle), out)


if __name__ == '__main__':
    unittest.main()