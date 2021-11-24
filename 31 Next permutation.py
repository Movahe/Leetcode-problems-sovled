"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory
"""
import unittest


class solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find longest non-increasing suffix

        right = len(nums) - 1
        while nums[right] <= nums[right -1] and right > 0:
            right -= 1

        if right == 0:
            return self.reverse(nums, 0, len(nums) -1)

        # find pivot

        pivot = right - 1
        for i in range(len(nums)-1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break

        # swap the pivot and successor
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        self.reverse(nums, pivot + 1, len(nums)-1)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


class testSolution(unittest.TestCase):
    def test0(self):
        nums = [1, 2, 3]
        output = [1, 3, 2]
        solution().nextPermutation(nums)
        assert nums == output

    def test1(self):
        nums = [3, 2, 1]
        output = [1, 2, 3]
        solution().nextPermutation(nums)
        assert nums == output

    def test2(self):
        nums = [1, 1, 5]
        output = [1, 5, 1]
        solution().nextPermutation(nums)
        assert nums == output


if __name__ == "__main__":
    unittest.main()
