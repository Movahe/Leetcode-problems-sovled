"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""


class Solution:
    def minPathSum(self, grid) -> int:
        """
        :param grid: List[List[int]]
        :return: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        # filling the first row
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        # filling the first column
        for j in range(1, m):
            grid[j][0] += grid[j - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]

    """
    Complexity Analysis

    Time complexity : O(mn). We traverse the entire matrix once.

    Space complexity : O(1). Do grid in-place, no extra space used
    """


grid = [[1, 2, 3], [4, 5, 6]]
res = Solution().minPathSum(grid)
assert res == 12