"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Note:

bisect(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in
argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in
the list, the right most position where element has to be inserted is returned. This function takes 4 arguments,
list which has to be worked with, number to insert, starting position in list to consider, ending position which
has to be considered.

bisect_left(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in
argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in the
list, the left most position where element has to be inserted is returned. This function takes 4 arguments, list which
has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered.

bisect_right(list, num, beg, end), similar to bisect. 
"""
import unittest
from bisect import bisect_left


class solution:
    def searchInsert(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

            if nums[mid] == target:  # nums[mid] == target, job done!
                return mid

        # What if the target value is not found? In this case, the loop will be stopped at the moment
        #   when right < left and nums[fight] < target < nums[left]. Hence, the proper position to
        #      insert the target is at the index left.
        return left

    # Time complexity: O(log N)
    # -- T(N) = a T(N/b) + O(N^d), where a = 1 due to that at each step, there is only one subproblem.
    # -- b = 2, its size is half of its initial problem. All this happens in a constant time, so d = 0
    # log_b a = 0 = d. O(N^{log_b a} log^d N) = O(N)

    # Space complexity: O(1): constant space solution.

    def searchInsert1(self, nums: list, target: int) -> int:
        return bisect_left(nums, target)


class testSolution(unittest.TestCase):
    def test0(self):
        nums = [1, 3, 5, 6]
        target = 5
        output = 2
        self.assertEqual(solution().searchInsert(nums, target), output)
        self.assertEqual(solution().searchInsert1(nums, target), output)

    def test1(self):
        nums = [1, 3, 5, 6]
        target = 2
        output = 1
        self.assertEqual(solution().searchInsert(nums, target), output)
        self.assertEqual(solution().searchInsert1(nums, target), output)

    def test2(self):
        nums = [1, 3, 5, 6]
        target = 7
        output = 4
        self.assertEqual(solution().searchInsert(nums, target), output)
        self.assertEqual(solution().searchInsert1(nums, target), output)


if __name__ == '__main__':
    unittest.main()