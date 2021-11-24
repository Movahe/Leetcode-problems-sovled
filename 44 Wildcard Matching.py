"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
"""
import unittest


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """

        :param s: string
        :param p: pattern, string
        :return: Bool
        """

        # init all matrix except [0][0] element as False
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        # for the top row, we set values to true until a non "*" character is found
        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = True
            else:
                break

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in {s[i-1], '?'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]

    # Time complexity: O(S⋅P) where S and P are lengths of the input string and the pattern respectively.
    # Space complexity:O(S⋅P) to store the matrix.


class testSolution(unittest.TestCase):
    def test0(self):
        s = 'aa'
        p = 'a?'
        output = True
        self.assertEqual(Solution().isMatch(s, p), output)

    def test1(self):
        s = 'aa'
        p = '*'
        output = True
        self.assertEqual(Solution().isMatch(s, p), output)

    def test2(self):
        s = 'cb'
        p = '?a'
        output = False
        self.assertEqual(Solution().isMatch(s, p), output)

    def test3(self):
        s = 'adceb'
        p = '*a*b'
        output = True
        self.assertEqual(Solution().isMatch(s, p), output)


if __name__ == '__main__':
    unittest.main()




