"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once
"""
import unittest


class Solution:
    def exist(self, board, word):
        """
        :param board: List[List[str]]
        :param word: str
        :return: bool
        """
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        for row in range(self.rows):
            for col in range(self.cols):
                if self.backtrack(row, col, word):
                    return True
        return False

    def backtrack(self, row, col, suffix):

        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.rows or col < 0 or col == self.cols \
                or self.board[row][col] != suffix[0]:
            return False

        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions (right, up, left, down)
        for rowoffset, coloffset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            # sudden-death return, no cleanup.
            if self.backtrack(row + rowoffset, col + coloffset, suffix[1:]):
                return True
        # revert the marking
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return False

    # Time complexity: O(N*3^L), where N is the number of cells in the board
    # and L is the length of the word to be matched.
    #   1). For the backtracking function, initially we could have at most 4 directions to explore, but further the
    #       choices are reduced into 3 (since we won't go back to where we come from).
    #   2). there could be N times invocation for the backtracking function in the worst case.
    # Space Complexity: O(L) where L is the length of the word to be matched.
    

class Solution_1:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.word = word
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                if self.backtrack(board, row, col, rows, cols, 0):
                    return True

        # no match found after all exploration
        return False

    def backtrack(self, board, row, col, rows, cols, start):
        word = self.word
        if start == len(word):
            return True

        if row < 0 or col < 0 or row == rows or col == cols or board[row][col] != word[start]:
            return False
        # prevent finding results including the head of the word
        board[row][col] = '#'
        found = False
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            found = self.backtrack(board, row + rowOffset, col + colOffset, rows, cols, start + 1)
            if found:
                break
        board[row][col] = word[start]

        return found


class testSolution(unittest.TestCase):
    def test0(self):

        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        output = True
        self.assertAlmostEqual(Solution().exist(board, word), output)

    def test1(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        output = True
        self.assertAlmostEqual(Solution_1().exist(board, word), output)


if __name__ == '__main__':
    unittest.main()