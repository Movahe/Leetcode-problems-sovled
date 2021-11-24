"""
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        print("\n matrix set zeros \n:")
        for k in range(R):
            print(matrix[k])

        return matrix

    # Time Complexity: O(M×N) where M and N are the number of rows and columns respectively.
    #
    # Space Complexity: O(M + N).

    def setZeroes_1(self, M):
        m, n = len(M[0]), len(M)
        r1 = any(M[0][j] == 0 for j in range(m))
        print("r1", r1)
        c1 = any(M[i][0] == 0 for i in range(n))
        print('c1', c1)
        for i in range(1, n):
            for j in range(1, m):
                if M[i][j] == 0:
                    M[i][0] = M[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if M[i][0] * M[0][j] == 0:
                    M[i][j] = 0

        if r1:
            for i in range(m):
                M[0][i] = 0

        if c1:
            for j in range(n):
                M[j][0] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print("\n matrix \n:")
for i in matrix:
    print(i)
res = Solution().setZeroes(matrix)
assert res == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

res1 = Solution().setZeroes_1(matrix)