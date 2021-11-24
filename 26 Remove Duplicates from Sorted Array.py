import unittest
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that 
each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed 
in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first 
k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place 
with O(1) extra memory.
"""


class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for j in range(len(nums)):
            if j > 0 and nums[j] == nums[j-1]:
                continue
            else:
                nums[i] = nums[j]
                i += 1
        return i

    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if len(nums) == 0:
            return 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1


L = [1, 1, 2, 2, 3, 3]
I = Solution().removeDuplicates(L)
print(L)
print(I)

"""
Time complexity : O(n). Assume that n is the length of array. Each of i and j traverses at most nn steps.
Space complexity: O(1).


"""
