"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Note: rotation a matrix 90 degrees == Transpose + reflect along the y axis.
"""
class Solution:
    def rotate(self, matrix):
        """
        :param matrix:  List[List[int]]
        :return: None, modify in place
        """
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix[0])
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            matrix[i].reverse()

    # Time complexity:O(n^2) each cell is getting read once and written once.
    # Space complexity: O(1) we do not use any other additional data structures.

