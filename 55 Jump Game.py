"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in
the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""


class Solution:
    def canJump(self, nums: list) -> bool:
        m = 0  # m tells the maximum index we can reach so far.
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
            if m >= len(nums) - 1:
                return True

    def canJump1(self, nums: list) -> bool:  #Going backward
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal

    # Time complexity: O(N)
    # Space complexity: O(1)

nums = [3, 2,1,0,4]
assert Solution().canJump(nums) == False
assert Solution().canJump1(nums) == False
