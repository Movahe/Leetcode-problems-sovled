"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Idea:
Since robot can move either down or right, there is only one path to reach the cells in the first row:
right->right->...->right.

The same is valid for the first column, though the path here is down->down-> ...->down.

What about the "inner" cells (m, n)? To such cell one could move either from the upper cell (m, n - 1),
or from the cell on the right (m - 1, n).
That means that the total number of paths to move into (m, n) cell is uniquePaths(m - 1, n) + uniquePaths(m, n - 1).

ex1:
Input: m = 3, n =7
Output: 28

ex2: m=3, n = 2
Output: 3

ex3:
input: m=7, n = 3
output: 28
"""
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    def uniquePaths_DP(self, m: int, n: int) -> int:
        d = [[1]*n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                d[row][col] = d[row-1][col] + d[row][col-1]
        return d[-1][-1]

    # Time complexity: O(M*N)
    # Space complexity: O(M*N)

    def uniquePaths_math(self, m: int, n: int) -> int:
        """
        :param m: int
        :param n: int
        :return: int
        Idea: Think this problem as a combinatorial problem. there are H+V moves to do from start to
        finish, H= n-1 horizontal moves, and V = m-1 vertical ones. One could choose when to move to right
        or choose to move down. so total possible ways to do is (H+V)!/H!V! .
        """
        return math.factorial(m+n-2) /(math.factorial(m-1)*math.factorial(n-1))

        """
        Time complexity: O( (M+N)* (Log(M+N)loglog(M+N))^2 )
        Space complexity: O(1).
        """


m, n = 3, 7
assert Solution().uniquePaths(m, n) == 28
assert Solution().uniquePaths_DP(m, n) == 28
assert Solution().uniquePaths_DP(m, n) == 28


