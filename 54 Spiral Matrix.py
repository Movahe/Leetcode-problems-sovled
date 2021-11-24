"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""


class Solution:
    def spiralOrder(self, matrix: list) -> list:
        res = []
        rows, cols = len(matrix), len(matrix[0])
        up = left = 0
        right = cols - 1
        down = rows - 1
        while len(res) < rows * cols:
            # traverse from left to right
            for col in range(left, right + 1):
                res.append(matrix[up][col])
            # traverse downwards
            for row in range(up + 1, down + 1):
                res.append(matrix[row][right])

            # make sure we are now on a different row
            if up != down:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[down][col])
            if left != right:
                for row in range(down - 1, up, -1):
                    res.append(matrix[row][left])
            left += 1
            right -= 1
            up += 1
            down -= 1
        return res

    # Time complexity: O(M*N), we have to visit every element once
    # Space complexity: O(M*N)

    def spiralOrder1(self, matrix: list) -> list:
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = [*zip(*matrix)][::-1]
        return res

    def spiralOrder2(self, matrix: list) -> list:
        res = []
        while matrix:
            # extend the top row
            res.extend(matrix.pop(0))
            # extend the right column
            if matrix:
                for i in range(len(matrix)):
                    if matrix[i]:
                        res.append(matrix[i].pop())
            # extend the bottom column
            if matrix:
                res.extend(matrix.pop()[::-1])
            # extend the left column
            if matrix:
                for i in range(len(matrix)-1, -1, -1):
                    if matrix[i]:
                        res.append(matrix[i].pop(0))
        return res







matrix = [[1,2,3],[4,5,6],[7,8,9]]
assert Solution().spiralOrder(matrix) == [1,2,3,6,9,8,7,4,5] == Solution().spiralOrder1(matrix)