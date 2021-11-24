"""
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
   1. Split the string into two non-empty substrings at a random index, i.e., if the string is s,
      divide it to x and y where s = x + y.
   2. Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step,
      s may become s = x + y or s = y + x.
   3. Apply step 1 recursively on each of the two substrings x and y.

Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

Ex 1:
Input: s1 = "great", s2 = "rgeat"
Output: true
"""
import unittest


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False

        # suppose only 3 letters left, a, b, and c.
        # All possible permutations of these 3 letters are scrambled string of each other.
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, n):
            if (f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) ) or (f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]) ):
                return True
        return False


class testsolution(unittest.TestCase):
    def test0(self):
        s1 = 'great'
        s2 = 'rgeat'
        self.assertAlmostEqual(Solution().isScramble(s1, s2), True)

    def test1(self):
        s1 = 'great'
        s2 = 'abcde'
        self.assertAlmostEqual(Solution().isScramble(s1, s2), False)


if __name__ == '__main__':
    unittest.main()