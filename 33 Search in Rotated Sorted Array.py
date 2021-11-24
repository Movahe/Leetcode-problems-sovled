"""
Given the array nums after the rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity

Note: a follow up question similar to this one is: 81. search in rotated sorted array II where there exists duplicates.
@ 81 Search in rotated sorted array II
"""
import unittest


class solution:
    def search(self, nums: list, target: int) -> int:
        """
        :param nums: List[int]
        :param target: int
        :return: int
        """

        begin = 0
        end = len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[end]:  # left side of mid is sorted
                if nums[begin] <= target < nums[mid]:  # target in the left side
                    end = mid - 1

                else:  # target in the right side
                    begin = mid + 1

            else: # right side is sorted
                if nums[mid] < target <= nums[end]:  # target in the right side
                    begin = mid + 1
                else:
                    end = mid - 1

        return -1


class testSolution(unittest.TestCase):
    def test0(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        output = 4
        self.assertEqual(solution().search(nums, target), output)

    def test1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        output = -1
        self.assertEqual(solution().search(nums, target), output)

    def test2(self):
        nums = [1]
        target = 0
        output = -1
        self.assertEqual(solution().search(nums, target), output)


if __name__ == '__main__':
    unittest.main()

