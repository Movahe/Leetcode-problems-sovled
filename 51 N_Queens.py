"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen
and an empty space, respectively.

idea: using the backtracking:
place the queens one by one, and when all possibilities are exhausted, backtrack by removing a queen
and placing it elsewhere.
"""


class Solution:
    def solveNQueens(self, n):
        # Making use of a helper function to get the
        # solutions in the correct output format
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def backtrack(row, diagonals, anti_diagonals, cols, state):
            # Base case - N queens have been placed
            if row == n:
                ans.append(create_board(state))
                return

            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                # If the queen is not placeable
                if (col in cols
                        or curr_diagonal in diagonals
                        or curr_anti_diagonal in anti_diagonals):
                    continue

                # "Add" the queen to the board
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                state[row][col] = "Q"

                # Move on to the next row with the updated board state
                backtrack(row + 1, diagonals, anti_diagonals, cols, state)

                # "Remove" the queen from the board since we have already
                # explored all valid paths using the above function call
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                state[row][col] = "."

        ans = []
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return ans


class Solution_DFS:
    def solveNQueens(self, n):

        res = []

        def dfs(queens, ddiff, ssum):
            p = len(queens)
            if p == n:
                queens = ['.' * i + 'Q' + '.' * (n - 1 - i) for i in queens]
                res.append(queens)
                return
            for q in range(n):
                if q in queens or p - q in ddiff or p + q in ssum:
                    continue
                dfs(queens + [q], ddiff + [p - q], ssum + [p + q])

        dfs([], [], [])
        return res


res = Solution().solveNQueens(4)
print(res)
res = Solution_DFS().solveNQueens(4)
print(res)