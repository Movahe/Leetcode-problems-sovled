"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
"""


# Start with the empty matrix, add the numbers in reverse order until we added the number 1.
# Always rotate the matrix clockwise and add a top row:

"""
    ||  =>  |9|  =>  |8|      |6 7|      |4 5|      |1 2 3|
                     |9|  =>  |9 8|  =>  |9 6|  =>  |8 9 4|
                                         |8 7|      |7 6 5|
"""

class Solution:
    def generateMatrix0(self, n):
        A, lo = [[n*n]], n*n
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [[*range(lo, hi)]] + [*zip(*A[::-1])]
        return A

    # https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions

    def generateMatrix(self, n):
        if not n:
            return []
        res = [[0 for _ in range(n)] for _ in range(n)]
        left, right, top, down, num = 0, n - 1, 0, n - 1, 1
        while left <= right and top <= down:
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
            top += 1
            for i in range(top, down + 1):
                res[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                res[down][i] = num
                num += 1
            down -= 1
            for i in range(down, top - 1, -1):
                res[i][left] = num
                num += 1
            left += 1
        return res

    def generateMatrix1(self, n):
        A = [[0]* n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k+1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, di
            i += di
            j += dj
        return A


matrix = Solution().generateMatrix0(3)
print(matrix)

