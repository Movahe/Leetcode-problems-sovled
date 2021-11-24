"""

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""
import unittest
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list) -> bool:
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True

        # Time complexity: O(N^2), because we need to traverse every position in the board,
        # and each of the four check steps is an O(1)O(1) operation.

        # Space complexity: O(N^2), because we need to create 3N arrays each with size N to
        # store all previously seen numbers for all rows, columns, and boxes.

    def isValidSudoku1(self, board: list) -> bool:
        rows = {}
        cols = {}
        boxes = {}
        for i in range(1, 10):
            rows[str(i)] = defaultdict(int)
            cols[str(i)] = defaultdict(int)
            boxes[str(i)] = defaultdict(int)

        current_box = 0
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    box_index = (i//3)*3 + j//3
                    rows[val][i] += 1
                    cols[val][j] += 1
                    boxes[val][box_index] += 1

                    if rows[val][i] > 1 or cols[val][j] > 1 or boxes[val][box_index] > 1:
                        return False

        return True


class testSolution(unittest.TestCase):
    def test0(self):
        board = [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        output = True
        self.assertEqual(Solution().isValidSudoku(board), output)
        self.assertEqual(Solution().isValidSudoku1(board), output)


    def test1(self):
        board = [["8","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        output = False
        self.assertEqual(Solution().isValidSudoku(board), output)
        self.assertEqual(Solution().isValidSudoku1(board), output)



if __name__ == '__main__':
    unittest.main()
