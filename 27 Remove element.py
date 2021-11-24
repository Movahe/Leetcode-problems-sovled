"""

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.

ex1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
import unittest


class solution1:
    def removeElement(self, nums: list, val: int):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

    def removeElement1(self, nums: list, val: int):
        i, j = 0, len(nums) - 1

        while i <= j:
            if nums[i] == val:
                nums[i], j = nums[j],  j - 1
                print("nums updated:", nums)
            else:
                i += 1
        return i

    def removeElement2(self, nums: list, val: int):
        while val in nums:
            nums.remove(val)
        return len(nums)


class testSolution(unittest.TestCase):
    def test0(self):
        nums = [3, 2, 2, 3]
        val = 3
        out = 2
        self.assertEqual(solution1().removeElement(nums, val), out)

    def test1(self):
        nums = [3, 2, 2, 3]
        val = 3
        out = 2
        self.assertEqual(solution1().removeElement1(nums, val), out)

    def test2(self):
        nums = [3, 2, 2, 3]
        val = 3
        out = 2
        self.assertEqual(solution1().removeElement2(nums, val), out)

    def test3(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2

        out = 5
        self.assertEqual(solution1().removeElement1(nums, val), out)

    def test4(self):
        nums = [3, 3, 3]
        val = 3

        out = 0
        self.assertEqual(solution1().removeElement2(nums, val), out)


if __name__ == '__main__':
    unittest.main()