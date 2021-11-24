"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Ex1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Ex2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Ex3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Ex4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000
"""

def findMedianSortedArrays(A, B) -> float:
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m

    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and B[j - 1] > A[i]:
            imin = i + 1

        elif i > 0 and A[i - 1] > B[j]:
            imax = i - 1

        else:
            if i == 0:

                max_of_left = B[j - 1]
            elif j == 0:
                max_of_left = A[i - 1]
            else:
                max_of_left = max(A[i - 1], B[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right)/2


'''M =[2, 3 , 4, 5]

N = list((2, 3, 4, 5, 6))

result = findMedianSortedArrays(M, N)
print(result)'''