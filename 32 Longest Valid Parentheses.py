"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
parentheses substring.

Ex1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Ex2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Ex3:
Input: s = ""
Output: 0
"""
import unittest


class solution:
    def longestValidParentheses(self, s):
        stack, res, s = [0], 0, ')'+s
        for i in range(1, len(s)):
            if s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
                res = max(res, i - stack[-1])
            else:
                stack.append(i)
        return res

    def longestValidParentheses1(self, s):  # yeah! Using stack method.
        # Step1: scan the string, start by pushing -1 onto the stack
        stack, res = [-1], 0
        for i in range(len(s)):
            # Step2, for every ‘(’ encountered, we push its index onto the stack.
            if s[i] == '(':
                stack.append(i)
            # 1) For every ')' encountered, pop the topmost element.
            # 2) If while pop stack, stack becomes empty, push the current element index into the stack.
            # 3) if while pop stack, stack is not empty, substrack the current element's index from the
            # top element of the stack, which gives the length of the currently encountered valid string of parentheses.
            elif s[i] == ')':
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    res = max(res, i-stack[-1])
        return res

        # Time comlexity: O(n), n is the length of the given string.
        # Space complexity: O(n), the size of stack can go up to n.

    def longestValidParentheses2(self, s): # Using two counters.
        left, right, max_length = 0, 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            if s[i] == ')':
                right += 1
            if right > left:
                left, right = 0, 0
            if left == right:
                max_length = max(max_length, 2*right)

        left, right = 0, 0
        for i in reversed(range(len(s))):
            if s[i] == ')':
                right += 1
            if s[i] == '(':
                left += 1
            if left > right:
                left, right = 0, 0
            if left == right:
                max_length = max(max_length, 2*left)

        return max_length

        # Time comlexity: O(n), n is the length of the given string.
        # Space complexity: O(1).

    def longestValidParenthese3(self, s):  # Using Dynamic programming.
        # Let dp[i] be the number of longest valid Parentheses ended with the i - 1 position of s
        # then dp[i + 1] = dp[p] + i + 1 - p, where p is the position of '(' which can matches current ')' in the stack.
        # s = ()(())
        dp, stack = [0]*(len(s) + 1), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i+1] = dp[p] + i - p + 1
        return max(dp)




class testSolution(unittest.TestCase):
    def test0(self):
        s = "(()"
        output = 2
        self.assertEqual(solution().longestValidParentheses(s), output)
        self.assertEqual(solution().longestValidParentheses1(s), output)
        self.assertEqual(solution().longestValidParentheses2(s), output)

    def test1(self):
        s = ")()())"
        output = 4
        self.assertEqual(solution().longestValidParentheses(s), output)
        self.assertEqual(solution().longestValidParentheses1(s), output)
        self.assertEqual(solution().longestValidParentheses2(s), output)

    def test2(self):
        s = ")("
        output = 0
        self.assertEqual(solution().longestValidParentheses(s), output)
        self.assertEqual(solution().longestValidParentheses1(s), output)
        self.assertEqual(solution().longestValidParentheses2(s), output)


if __name__ =="__main__":
    unittest.main()





