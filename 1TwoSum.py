import unittest
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class solution:
    def two_sum0(self, nums, target: int):
        for i, x in enumerate(nums[:-1]):
            for j, y in enumerate(nums[i+1:]):
                if x + y == target:
                    return i, i + 1 + j

    def two_sum1(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in h:
                h[num] = i
            else:
                return h[diff], i


class testSolution(unittest.TestCase):
    def test0(self):
        nums = [3, 2, 4]
        target = 6
        out = (1, 2)
        self.assertEqual(solution().two_sum0(nums, target), out)
        self.assertEqual(solution().two_sum1(nums, target), out)

    def test1(self):
        nums = [2, 7, 11, 20]
        target = 9
        out = (0, 1)
        self.assertEqual(solution().two_sum0(nums, target), out)
        self.assertEqual(solution().two_sum1(nums, target), out)

    def test2(self):
        nums = [3, 11, 3,  20]
        target = 6
        out = (0, 2)
        self.assertEqual(solution().two_sum0(nums, target), out)
        self.assertEqual(solution().two_sum1(nums, target), out)


if __name__ == "__main__":
    unittest.main()

