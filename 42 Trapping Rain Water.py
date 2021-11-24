"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
water it can trap after raining.
"""

class Solution:
    def trap(self, height):
        """
        :param height: List[int]
        :return: int
        """
        ans = 0
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                    # print("new added area from left:",left_max - height[left])
                    # print("ans_update from left:", ans)
                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                    # print("new added area from right:", right_max - height[right])
                    # print("ans_update from right:", ans)
                right -= 1
        return ans

    # Space complexity: O(1) extra space.
    # Time complexity: O(N) traveling the whole array. 

height = [0,1,0,2,1,0,1,3,2,1,2,1]
res = Solution().trap(height)
assert res == 6