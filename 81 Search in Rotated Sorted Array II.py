"""

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the
resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums,
or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Note: this question is similar to question 33: Search in rotated Sorted array
"""
import unittest


class Solution:
    def search(self, nums, target: int) -> bool:
        """
        :param nums: List[int]
        :param target: int
        :return: bool
        """
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                return True

            while end > mid and nums[end] == nums[mid]: # to take care of multiple duplicates.
                end -= 1

            # left side of mid is sorted
            if nums[mid] > nums[end]:
                if nums[begin] <= target < nums[mid]:  # target in the left side
                    end = mid - 1

                else:  # target in the right side
                    begin = mid + 1

            else:  # right side is sorted
                if nums[mid] < target <= nums[end]:  # target in the right side
                    begin = mid + 1
                else:
                    end = mid - 1

        return False

    # Time complexity: O(N) worst case, O(log N) best case, where N is the length of the input array.
    # Worst case: this happens when all the elements are the same and we search for some different element,
    # at each step we will only be able to reduce the search space by 1.
    # Best case: this happens when all the elements are distinct. At each step we will be able to divide our
    # search space by half
    # Space complexity: O(1)


class testSolution(unittest.TestCase):
    def test0(self):
        nums = [2, 5, 6, 0, 0, 1, 2]
        target = 3
        output = False
        self.assertAlmostEqual(Solution().search(nums, target), output)

    def test1(self):
        nums = [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1]
        target = 2
        output = True
        self.assertAlmostEqual(Solution().search(nums, target), output)


if __name__ == "__main__":
    unittest.main()





