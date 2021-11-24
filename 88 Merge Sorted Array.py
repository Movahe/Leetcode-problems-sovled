"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
 the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To
accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""
import unittest


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        :param nums1: List[int]
        :param m:
        :param nums2: List[int]
        :param n:
        :return:  Do not return anything, modify nums1 in-place instead.

        """
        for i in range(n):
            nums1[i+m] = nums2[i]
        nums1.sort()
    # Time complexity: O((m+n)log(m+n)), built-in algo to sort is O(xlogx). After the merging of two list,
    # total length is m+n.
    # Space complexity: O(n)

    def merge_three_pointers(self, nums1, m: int, nums2, n: int) -> None:
        nums1_copy = nums1[:m]
        i, j = 0, 0
        for k in range(m+n):
            if j >= n or (i < m and nums1_copy[i] <= nums2[j]):
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
    # Complexity Analysis
    # Time complexity : O(n+m).
    # We are performing n+2*m reads and n+2*m writes. Because constants are ignored in Big O notation,
    # this gives us a time complexity of O(n+m).
    #
    # Space complexity :O(m).
    # We are allocating an additional array of length mm.

    # Interview Tip: Whenever you're trying to solve an array problem in-place, always consider the possibility of
    # iterating backwards instead of forwards through the array. It can completely change the problem, and make it a
    # lot easier.

    def merge_three_pointers_from_back(self, nums1, m, nums2, n):
        p1, p2 = m-1, n - 1
        for p in range(m+n-1, -1, -1):
            if p2 < 0:
                break
            if p1>= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

        # Time complexity: O(m+n).
        # Space complextiy: O(1), we are not use extra array.


class testSolution(unittest.TestCase):
    def test0(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        output = [1,2,2,3,5,6]
        Solution().merge(nums1, m, nums2, n)
        assert nums1 == output

    def test1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        output = [1,2,2,3,5,6]
        Solution().merge_three_pointers(nums1, m, nums2, n)
        assert nums1 == output

    def test2(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        output = [1,2,2,3,5,6]
        Solution().merge_three_pointers_from_back(nums1, m, nums2, n)
        assert nums1 == output

if __name__ == '__main__':
    unittest.main()