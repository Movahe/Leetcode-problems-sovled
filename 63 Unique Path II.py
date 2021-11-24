"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        """
        :param obstacleGrid: List[List[int]]
        :return: int
        """
        # if the starting cell has an obstacle, then no paths to the destination
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1  # number of ways of reaching the starting cell = 1

        # Filling the first row
        for i in range(1, n):
            # dp[0][i] = int(obstacleGrid[0][i] ==0 and dp[0][i-1]
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i - 1]

        # Filling the first column
        for j in range(1, m):
            # or simply dp[j][0] = int(obstacleGrid[j][0]==0 and dp[j-1][0])
            if obstacleGrid[j][0] == 1:
                dp[j][0] = 0
            else:
                dp[j][0] = dp[j - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0

        return dp[-1][-1]

    """
    Complexity analysis
    Time complexity: O(M*N) we process each cell just once
    Space complexity: O(M*N) dp array m*n. alternatively, once could use obstacleGrid as the dp array then
    no extra space.  in that case , space complexity is O(1).
    """