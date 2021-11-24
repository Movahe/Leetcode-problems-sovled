"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Ex1:
Input: nums = [1, 2, 2]
Output: [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]

Ex2:
Input: nums = [0]
Output: [[], [0]]
"""
import unittest

class Solution:  # Recursion/Cascading
    def subsetsWithDup(self, nums: list) -> list:
        res = [[]]
        nums.sort()
        size = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                l = len(res)
            for j in range(len(res)-l, len(res)):
                res.append(res[j]+[nums[i]])

        return res

    def subsetsWithDup_1(self, nums: list) -> list:
        nums, res, pos = sorted(nums), [[]], {}
        for n in nums:
            start, l = pos.get(n, 0), len(res)
            res += [r+[n] for r in res[start:]]
            pos[n] = l
        return res

    # Time complexity: O(n*2^n) n times 2 to the power of n
    # sort adds O(n log n). Two for loops to create all possible subsets. worst case must create 2^n subsets.
    # Space complexity: O(log n)

    def subsetswithDup_DFS(self, nums: list) -> list:

        def dfs(nums, path, res):
            res.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:  # very useful trick to skip duplicates.!
                    continue
                dfs(nums[i+1:], path+[nums[i]], res)

        res = []
        nums.sort()
        dfs(nums, [], res)
        return res


class testSolution(unittest.TestCase):
    def test0(self):
        nums = [1, 2, 2]
        res = [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
        self.assertAlmostEqual(Solution().subsetsWithDup(nums), res)
        self.assertAlmostEqual(Solution().subsetsWithDup_1(nums), res)
        output = Solution().subsetswithDup_DFS(nums)
        print(output)

    def test1(self):
        nums = [1, 1, 1]
        res = [[], [1], [1, 1], [1, 1, 1]]
        self.assertAlmostEqual(Solution().subsetsWithDup(nums), res)
        self.assertAlmostEqual(Solution().subsetsWithDup_1(nums), res)
        output = Solution().subsetswithDup_DFS(nums)
        print(output)

if __name__ == '__main__':
    unittest.main()
