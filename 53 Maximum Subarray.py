"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which
has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Ex 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
import math


class Solution:
    def maxSubarray(self, nums: list)->int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)

        return max_subarray

    # Time complexity: O(N^2) where N in the len(nums)
    # Space complexity: O(1) we only use 2 variables: ans and current_subarray.

    def maxSubarray1(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        newNum = maxTotal = nums[0]
        for i in range(1, len(nums)):
            newNum = max(nums[i], nums[i] + newNum)
            maxTotal = max(newNum, maxTotal)
        return maxTotal

    # Time complexity: O(N), iterate through every element of nums exactly once.
    # Space complexity: O(1), only use 2 variables.

    def maxSubarray2(self, nums: list) -> int:  # modify the nums in-place.
        if len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
assert Solution().maxSubarray1(nums) == 6 == Solution().maxSubarray2(nums)
print(nums)
