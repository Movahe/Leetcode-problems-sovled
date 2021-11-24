"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.
"""
import math
import unittest


class Solution:
    def largestRectangleArea_1(self, heights):
        """

        :param heights: List[int]
        :return: int
        # brute force: Time complexity: O(N^3), we have to find the minimum height bar O(N)
          lying between every pair O(N^2)
        # Space complexity O(1), constant space is used.
        """
        max_area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                min_height = math.inf
                for k in range(i, j+1):
                    min_height = min(min_height, heights[k])
                max_area = max(max_area, min_height*(j - i + 1))
        return max_area

    def largestRectangleArea_2(self, heights):
        max_area = 0
        for i in range(len(heights)):
            min_height = math.inf
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height*(j-i+1))
        return max_area

    # brute force: Time complexity: O(N^2), every pair O(N^2) is considered.
    # Space complexity O(1), constant space is used.

    # Divide and conquer: This approach relies on the observation that the rectangle with maximum area
    # will be the maximum of:
    # 1). The widest possible rectangle with height equal to the height of the shortest bar.
    # 2). The largest rectangle confined to the left of the shortest bar(subproblem).
    # 3). The largest rectangle confined to the right of the shortest bar(subproblem).

    def largestRectangleArea_3(self, heights):
        def calculateArea(heights, start, end):
            if start > end:
                return 0
            min_index = start
            for i in range(start, end+1):
                if heights[min_index] > heights[i]:
                    min_index = i
            return max(heights[min_index]*(end-start+1),
                       calculateArea(heights, start, min_index-1),
                       calculateArea(heights, min_index+1, end),
                       )
        return calculateArea(heights, 0, len(heights)-1)

    # Complexity Analysis
    #
    # Time complexity : Average Case: O(NlogN).
    #
    # Worst Case: O(N^2)). If the numbers in the array are sorted, we don't gain the advantage of divide and conquer.
    #
    # Space complexity : O(n). Recursion with worst case depth nn.

    # Using stack
    def largestRectangleArea_4(self, heights):
        # The zero serves a couple functions:
        # It always adds the first height to the stack so it's not empty
        # In the case where the given heights are all in ascending order, it creates an ending point that breaks
        # this trend, allowing us to calculate the areas
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            # keep stacking until we find the descending oder of height in heights.
            # While condition is true when we see a height that's smaller than height stored at the top of the stack.
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # Key thing to remember here is that stack is always ascending, so i-1 represents the right boundary of
                # the considered rectangle and stack[-1] represents the left boundary. So subtracting the them
                # gets you the width!
                w = i - stack[-1] - 1
                ans = max(ans, h*w)
            stack.append(i)
        heights.pop()
        return ans

    # Complexity Analysis

    # Time complexity : O(n). nn numbers are pushed and popped.
    # Space complexity : O(n). Stack is used.


class testSolution(unittest.TestCase):
    def test0(self):
        heights = [2, 1, 5, 6, 2, 3]
        output = 10
        self.assertAlmostEqual(Solution().largestRectangleArea_1(heights), output)
        self.assertAlmostEqual(Solution().largestRectangleArea_2(heights), output)
        self.assertAlmostEqual(Solution().largestRectangleArea_3(heights), output)
        self.assertAlmostEqual(Solution().largestRectangleArea_4(heights), output)


if __name__ == '__main__':
    unittest.main()

