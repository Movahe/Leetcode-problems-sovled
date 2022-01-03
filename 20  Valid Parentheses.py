"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the
input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
import unittest


class Solution:
    def isValid(self, s: str) -> bool:

        d = {0:None, '(':')', '{':'}', '[':']'}
        stack = [0]
        for i in s:
            if i in d:
                stack.append(i)
            elif d[stack.pop()] != i:
                return False

        return stack == [0]
    # Time comlexity: O(N)
    # Space complexity: O(N)


class TestSolution(unittest.TestCase):
    def test0(self):
        input = '()'
        out = True
        self.assertEqual(Solution().isValid(input), out)

    def test1(self):
        input = '([{}])'
        out = True
        self.assertEqual(Solution().isValid(input), out)

    def test2(self):
        input = '([}])'
        out = False
        self.assertEqual(Solution().isValid(input), out)

    def test3(self):
        input = "([)]"
        out = False
        self.assertEqual(Solution().isValid(input), out)


if __name__ == '__main__':
    unittest.main()

