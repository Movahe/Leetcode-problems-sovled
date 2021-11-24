"""

Write an efficient algorithm that searches if a value exist in an m x n matrix.
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        """

        :param matrix:  List[List[int]]
        :param target: int
        :return: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # binary search
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False

    # Time complexity: O(log m*n), binary search
    # Space complexity: O(1)


matrix = [[1, 3, 5, 7],
          [10, 11, 16, 20],
          [23, 30, 34, 60]]
target = 3
res = True
assert res == Solution().searchMatrix(matrix, target)