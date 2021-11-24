"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations
in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

"""
import unittest
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:  # recursive call
        res = []

        # Sorting is really helpful, se we can avoid over counting easily
        candidates.sort()
        # print("sorted candidates:", candidates)
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, start, comb, res):
        if target < 0:
            return  # backtracking

        if target == 0:
            res.append(comb)
            return

        for i in range(start, len(nums)):
            # To avoid over-counting, we just ignore the duplicates after the first element.
            if i > start and nums[i] == nums[i-1]:
                continue

            # If the current element is bigger than the assigned target, there is
            # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
                break
            # We change the start to `i + 1` because one element only could be used once, so we go to next.
            self.dfs(nums, target - nums[i], i+1, comb + [nums[i]], res)


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
res = Solution().combinationSum2(candidates, target)

assert res == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

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