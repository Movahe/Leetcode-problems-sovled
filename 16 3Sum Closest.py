import unittest

"""
Given an integer array nums of length n and an integer target, find three integers in nums such that 
the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
"""


# using the brutal force, the time complexity is O(n^3), while space comlexity is O(1)


class solution0:
    def threeSumClosest(self,nums, target):
        nums.sort()
        min_target = float('inf')

        for i in range(len(nums) -2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if abs(nums[i] + nums[j] + nums[k]) <= abs(min_target):
                        min_target = nums[i] + nums[j] + nums[k] - target
        return min_target + target


# using the two pointers, the time complexity is O(n^2), time complexity is O(1)
class solution1:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            j, k = i+1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum < target:
                    j += 1
                if sum > target:
                    k -= 1
        return result


class TestSolution0(unittest.TestCase):
    def test0(self):
        nums = [-1, 2, 1, -4]
        target = 1
        output = 2
        self.assertEqual(solution0().threeSumClosest(nums, target), output)

    def test1(self):
        nums = [0, 0, 0]
        target = 1
        output = 0
        self.assertEqual(solution0().threeSumClosest(nums, target), output)


class TestSolution1(unittest.TestCase):
    def test0(self):
        nums = [-1, 2, 1, -4]
        target = 1
        output = 2
        self.assertEqual(solution1().threeSumClosest(nums, target), output)

    def test1(self):
        nums = [0, 0, 0]
        target = 1
        output = 0
        self.assertEqual(solution1().threeSumClosest(nums, target), output)


if __name__ == '__main__':
    unittest.main()