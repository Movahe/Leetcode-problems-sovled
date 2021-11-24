"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
import unittest


class solution:
    def searchRange(self, nums: list, target: int) -> list:
        if target not in nums:
            return [-1, -1]
        n, i, j = len(nums), -1, -1
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                i, j = mid, mid
                while i - 1 >= 0 and nums[i - 1] == target:
                    i -= 1
                while j + 1 < n and nums[j + 1] == target:
                    j += 1
                break
        return [i, j]


class testSolution(unittest.TestCase):
    def test0(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        output = [3, 4]
        self.assertEqual(solution().searchRange(nums, target), output)

    def test1(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        output = [-1, -1]
        self.assertEqual(solution().searchRange(nums, target), output)

    def test2(self):
        nums = [ ]
        target = 6
        output = [-1, -1]
        self.assertEqual(solution().searchRange(nums, target), output)


if __name__ == '__main__':
    unittest.main()