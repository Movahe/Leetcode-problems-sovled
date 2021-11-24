"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique
element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed
in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the
first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1)
extra memory.
"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        """
        :param nums:  List[int]
        :return: int
        """
        i, count = 1, 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1

                if count > 2:
                    nums.pop(i)  # pop the unwanted duplicates.
                    i -= 1

            else:
                count = 1

            i += 1

        return len(nums)

    # Complexity Analysis
    #
    # Time Complexity: Let's see what the costly operations in our array are:
    # We have to iterate over all the elements in the array. Suppose that the original array contains N elements,
    # the time taken here would be O(N).
    # Next, for every unwanted duplicate element, we will have to perform a delete operation
    # and deletions in arrays are also O(N).
    # The worst case would be when all the elements in the array are the same.
    # In that case, we would be performing N - 2N−2 deletions thus giving us O(N^2)
    # Overall complexity = O(N) + O(N^2) \equiv O(N^2)
    # Space Complexity: O(1)O(1) since we are modifying the array in-place.

    def removeDuplicates_two_pointers(self, nums) -> int:
        j, count = 1, 1
        # Start from the second element of the array and process elements one by one.
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                # If the current element is a duplicate, increment the count.
                count += 1
            else:
                # Reset the count since we encountered a different element than the previous one
                count = 1

            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j

        # Complexity Analysis

        # Time Complexity: O(N) since we process each element exactly once.
        # Space Complexity: O(1)


nums = [1,1,1,2,2,3]
number = 1
J = Solution().removeDuplicates_two_pointers(nums)
print(nums[:J])