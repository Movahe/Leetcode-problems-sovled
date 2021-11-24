"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:                     Ex2:                         Ex3:
Input: nums = [1,2,0]       Input: nums = [3,4,-1,1]    Input: nums = [7,8,9,11,12]
Output: 3                   Output: 2                   Output: 1
"""
import unittest


class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        """
        :param nums:  List[int]
        :return: int
        Basic idea:
        1. For any array whose length is l, the first missing positive must be in range [1,...,l+1],
        so we only have to care about those elements in this range and remove the rest.
        2. We can use the array index as the hash to restore the frequency of each number within
         the range [1,...,l+1]
        """

        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):  # Replace those negative elements with zero.
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        print(nums)
        for i in range(len(nums)): # Use the index as the hash to record the frequency of each number
            nums[ nums[i] % n] += n
            # % is the modulus
            # num[i]%n will get original number, num[i] //n will get the frequency of the number i.
        print("\nnums:\n", nums)

        for i in range(1, len(nums)):
            if nums[i]//n == 0:
                return i
        return n


class Solution1:
    def firstMissingPositive(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        n = len(nums)
        # Base case:
        if 1 not in nums:
            return 1

        # nums = [1]
        if n == 1:
            return 2

        # Replace negative numbers, zeros, and numbers that are larger than n by 1s.
        # nums will only contain positive numbers
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # Use index as a hash key and number sign as a presence detector
        # for ex, if nums[1] is negative, that means number 1 is in the array
        # for ex, if nums[2] is positive - number 2 is missing
        for i in range(n):
            a = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == n:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])
        # Now the index of the first positive number
        # is equal to first missing positive.
        for i in range(1, n):
            for i in range(1, n):
                if nums[i] > 0:
                    return i
        if nums[0] > 0:
            return n
        return n + 1


nums = [3, 4, 1, 5]
nums1 = [3, 4, 1, 5]

i = Solution().firstMissingPositive(nums)
assert i == 2
assert 2 == Solution1().firstMissingPositive(nums1)


# example of Hash and unHashed map:
L = [1, 1, 1, 2, 2]
size = len(L)
for e in L:
    L[e%size] += size

print('Hashed:', L)  # [1, 16, 11, 2, 2]

unhashed = L.copy()
for i, e in enumerate(unhashed):
    unhashed[i] = e % size

print("unHashed:", unhashed)  # unHashed: [1, 1, 1, 2, 2]
print("\nFrequency \n")
for i, e in enumerate(L):
    i_count = e//size
    print(f'{i}:{i_count}')

# 0: 0
# 1: 3
# 2: 2
# 3: 0
# 4: 0