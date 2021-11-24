"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's
and return its area.
"""

class Solution:
    def maximalRectangle(self, matrix) -> int:
        """

        :param matrix: List[List[str]]
        :return: int
        """
        max_area = 0
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '0':
                    continue

                # compute the maximum width and update dp with it
                width = dp[row][col] = dp[row][col - 1] + 1 if col else 1
                # compute the maximum area rectangle with a lower right corner at [row, col]
                for k in range(row, -1, -1):
                    width = min(width, dp[k][col])
                    max_area = max(max_area, width*(row-k+1))
        return max_area

        # Complexity Analysis

        # Time complexity : O(N^2 M). Computing the maximum area for one point takes O(N) time, since it iterates over
        # the values in the same column. This is done for all N * M points, giving O(N) * O(N*M) = O(N^2 M)

        # Space complexity : O(NM). We allocate an equal sized array to store the maximum width at each point.

    def maximalRectangle_stack(self, matrix) -> int:
        def max_area_in_histogram(heights):
            heights.append(0)
            stack = [-1]
            max_area = 0
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    max_area = max(max_area, height*(i - stack[-1] -1))
                stack.append(i)

            heights.pop()
            return max_area


        if not matrix:
            return 0
        max_area = 0
        dp = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # update the state of this row's histogram using the last row's histogram
                # by keeping track of the number of consecutive ones
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
                # update max_area with the maximum area from this row's histogram
            max_area = max(max_area, max_area_in_histogram(dp))
        return max_area

    # Complexity analysis
    # Time complexity: O(N*M), go thorough each row takes M(length of each row) time This is done
    # N times for O(NM)
    # Space complexity: O(M), we allocate an array of size of the number of columns to store our widths at each row.


matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
res = Solution().maximalRectangle(matrix)
res1 = Solution().maximalRectangle_stack(matrix)
assert res == 6
assert res1 == 6