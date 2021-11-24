import unittest

"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, 
which, together with the x-axis forms a container, such that the container contains the most water.
"""

class solution0:
    def maxArea(self, height):

        max_area = 0
        L, R = 0, len(height) -1

        while L != R:
            max_area = max(max_area, min(height[R], height[L])*(R-L))

            if height[L] < height[R]:
                L += 1
            else:

                R -= 1

        return max_area


class solution1:
    def maxArea(self, height):
        max_area = 0
        i, n = 0, len(height)
        while i < n:
            j = i + 1
            while j < n:
                max_area = max(max_area, min(height[i], height[j])*(j - i))
                j += 1
            i += 1

        return max_area


class TestSolution(unittest.TestCase):
    def test1(self):
        height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        height2 = [1, 1]
        self.assertEqual(solution0().maxArea(height1), 49)
        self.assertEqual(solution0().maxArea(height2), 1)

    def test2(self):
        height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        height2 = [1, 1]
        self.assertEqual(solution1().maxArea(height1), 49)
        self.assertEqual(solution1().maxArea(height2), 1)


if __name__ == "__main__":
    unittest.main()


