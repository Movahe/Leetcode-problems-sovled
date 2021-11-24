"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
such that:
i). 0 <= a, b, c, d < n
ii). a, b, c, and d are distinct.
iii). nums[a] + nums[b] + nums[c] + nums[d] == target

Time Complexity:
O(n^(k−1) ), or O(n^3) for 4Sum. We have k - 2 loops, and twoSum is O(n).
Space Complexity: O(n). We need O(k) space for the recursion.
"""

import unittest


class kSum_solution:
    def fourSum(self, nums, target):
        def kSum(nums, target, k):
            res = []

            if len(nums) == 0 or nums[0]*k > target or nums[-1]*k < target:
                return res

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i+1:], target - nums[i], k-1):
                        res.append([nums[i]] + subset)
            return res

        def twoSum(nums, target):
            res = []
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                current_sum = nums[lo] + nums[hi]
                if current_sum < target or (lo > 0 and nums[lo] == nums[lo-1]):
                    lo += 1
                elif current_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi+1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)
    

class TestKSumSolution(unittest.TestCase):
    def test0(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        out = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        self.assertEqual(kSum_solution().fourSum(nums, target), out)

    def test1(self):
        nums = [2, 2, 2, 2, 2]
        target = 8
        out = [[2, 2, 2, 2]]
        self.assertEqual(kSum_solution().fourSum(nums, target), out)


if __name__ == '__main__':
    unittest.main()






























