"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses

Ex1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Ex2:
Input: n = 1
Output: ["()"]

"""
from itertools import combinations_with_replacement, product
import numpy as np
import unittest


class solution:
    def generateParenthesis0(self, n: int):
        """

        :param n: total number of pairs of parentheses
        :return  List[str]: all combinations of well-formed parentheses.
        """
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left - 1, right)

            if right > left:
                generate(p + ')', left, right - 1)

            if right == 0:
                parens.append(''.join(p))
            return parens

        return generate('', n, n)

    def generateParenthesis1(self, n: int):
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left - 1, right):
                    yield q
                for q in generate(p + ')', left, right - 1):
                    yield q
        return list(generate('', n, n))

    def generateParenthesis2(self, n, open=0):
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis2(n - 1, open + 1)] + \
                   [')' + p for p in self.generateParenthesis2(n, open - 1)]
        return [')' * open] * (not n)


class DFS_solution1:
    def generateParenthesis(self, n: int):
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left, right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        if right < left:
            return
        if not left and not right:
            ans.append(string)
            return
        if left:
            self.dfs(left-1, right, ans, string + '(')
        if right:
            self.dfs(left, right-1, ans, string + ')')


"""
This is a visualization of the above DFS search. Using n=2 as an example:

dfs(2, 2, [], "")
        dfs(1, 2, [], "(")
                dfs(0, 2, [], "((")
                        dfs(0, 1, [], "(()")
                                dfs(0, 0, [], "(())") # We got "(())" and we append it to ans
                dfs(1, 1, ["(())"], "()")
                        dfs(0, 1, ["(())"], "()(")
                                dfs(0, 0, ["(())"], "()()") # We got "(())" and we append it to ans
                        dfs(1, 0, ["(())", "()()"], "())") # will just return as right < left
        dfs(2, 1, ["(())", "()()"], ")") # will just return as right < left
"""


class DFS_solution2:
    def generateParenthesis(self, n: int):
        res = []

        def dfs(l, r, path, res):
            if r < l or l == -1 or r == -1:
                return
            if l == 0 and r == 0:
                res.append(path[:])
            else:
                dfs(l-1, r, path + "(", res)
                dfs(l, r-1, path + ")", res)
        dfs(n, n, "", res)
        return res


class testSolution(unittest.TestCase):
    def test0(self):
        n = 3
        out = ["((()))","(()())","(())()","()(())","()()()"]
        self.assertEqual(solution().generateParenthesis0(n), out)
        self.assertEqual(solution().generateParenthesis1(n), out)
        self.assertEqual(solution().generateParenthesis2(n), out)

    def test1(self):
        n = 2
        out = ["(())","()()"]
        self.assertEqual(solution().generateParenthesis0(n), out)
        self.assertEqual(solution().generateParenthesis1(n), out)
        self.assertEqual(solution().generateParenthesis2(n), out)


class test_DFS_solutions(unittest.TestCase):
    def test0(self):
        n = 3
        out = ["((()))","(()())","(())()","()(())","()()()"]
        self.assertEqual(DFS_solution1().generateParenthesis(n), out)
        self.assertEqual(DFS_solution2().generateParenthesis(n), out)

    def test0(self):
        n = 2
        out = ["(())","()()"]
        self.assertEqual(DFS_solution1().generateParenthesis(n), out)
        self.assertEqual(DFS_solution2().generateParenthesis(n), out)


if __name__ == '__main__':
    unittest.main()




