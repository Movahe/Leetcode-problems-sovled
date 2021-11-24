class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diags, anti_diags):
            if row == n:
                return 1
            solution = 0
            for col in range(n):
                ddif = row - col
                ssum = row + col
                if col in cols or ddif in diags or ssum in anti_diags:
                    continue
                cols.add(col)
                diags.add(ddif)
                anti_diags.add(ssum)
                solution += backtrack(row+1, cols, diags, anti_diags)
                cols.remove(col)
                diags.remove(ddif)
                anti_diags.remove(ssum)
            return solution
        return backtrack(0, set(), set(), set())


class Solution_dfs:
    def totalNQueens(self, n: int) -> int:
        res = []
        def dfs(queens, ddif, ssum):
            row = len(queens)
            if row == n:
                temp = [['.'*i + 'queen' + '.'*(n-i-1)]for i in queens ]
                res.append(temp)
            for col in range(n):
                if col in queens or row - col in ddif or row + col in ssum:
                    continue
                dfs(queens+[col], ddif+[row - col], ssum+[row+col])

        dfs([], [], [])
        return len(res)


assert Solution().totalNQueens(4) == Solution_dfs().totalNQueens(4) == 2