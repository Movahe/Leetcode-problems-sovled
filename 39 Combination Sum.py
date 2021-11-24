"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.

"""
import unittest


class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        res = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # find the combination that the sum is the target
                res.append(list(comb))
            elif remain < 0:
                # exceed the scope, stop the exploration
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                # give the current number another chance, rather moving on
                backtrack(remain-candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return res


class DFS_solution:
    def combinationSum(self, candidates, target):
        res = []
        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, nums, target, comb, res):
        if target < 0:
            return
        if target == 0:
            res.append(comb)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], comb + [nums[i]], res)

    # Time complexity: O(N^(M/min_cand + 1)), N = len(candidates), M = target, min_cand = min(candidates)
    # Space complexity: O(M/min_cand)


class testSolution(unittest.TestCase):
    def test0(self):
        candidates = [2, 3, 6, 7]
        target = 7
        output = [[2, 2, 3], [7]]
        self.assertEqual(Solution().combinationSum(candidates, target), output)
        self.assertEqual(DFS_solution().combinationSum(candidates, target), output)

    def test1(self):
        candidates = [2, 3, 5]
        target = 8
        output = [[2,2,2,2],[2,3,3],[3,5]]
        self.assertEqual(Solution().combinationSum(candidates, target), output)
        self.assertEqual(DFS_solution().combinationSum(candidates, target), output)


    def test2(self):
        candidates = [2]
        target = 1
        output = []
        self.assertEqual(Solution().combinationSum(candidates, target), output)
        self.assertEqual(DFS_solution().combinationSum(candidates, target), output)


if __name__ == "__main__":
    unittest.main()


"""
DFS solutions/templates to 6 different classic backtracking problems & more
39 Combination Sum
40. Combination Sum II
78. Subsets
90. Subsets II
46. Permutations
47. Permutations II

More good backtracking problems for practice:
131. Palindrome Partitioning
784. Lettercase Permutation
1087. Brace Expansion
93. Restore IP addresses
1079 Letter Tile Possibilities
"""

