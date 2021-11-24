"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index
"""
import unittest
import math
from functools import lru_cache


@lru_cache(None)


class solution:  # Greey approach.
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r+1))
            # nxt is the farthest position that all positions in [left, right] can reach.
            l, r = r + 1, nxt
        return times

    # Time: O(N), where N <= 1000 is the length of array nums
    # Space: O(1)


nums = [2, 3, 1, 1, 4]
steps = solution().jump(nums)
assert 2 == steps


