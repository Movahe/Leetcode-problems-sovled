"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Ex1:
Input: n = 4, k=2
output = [[1, 2],
          [1, 3],
          [1, 4],
          [2, 3],
          [2, 4],
          [3, 4]]
"""
import unittest


class Solution:
    def combine_dfs(self, n: int, k: int):
        """
        :param n: int
        :param k: int
        :return:  List[List[int]]
        """
        L = [i for i in range(1, n+1)]

        def dfs(L, k, path, res):
            if k == 0:
                res.append(path)
                return
            for i, val in enumerate(L):
                dfs(L[i+1:], k - 1, path + [val], res)

        res = []
        dfs(L, k, [], res)
        return res if res else []

    def combine_backtrack(self, n, k):

        def backtrack(first=1, path=[]):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(first, n+1):
                path.append(i)
                backtrack(i+1, path)
                path.pop()

        res = []
        backtrack()
        return res
    # Time complexity : O( k N!/(N-k)!k! )
    # ​
    # Space complexity: O(k N!/(N-k)!k!) to keep all the combinations for an output.

    # Lexicographic(binary sorted combinations)
    #   4, 3, 2, 1      4, 3, 2, 1
    #   0, 0, 1, 1      0, 1, 0, 1
    #       [1, 2]          [1, 3]
    def combine_binary(self, n, k):
        nums = list(range(1, k+1)) + [n+1]
        print(nums)
        output, j = [], 0
        while j < k:
            # add curent combination
            output.append(nums[:k])
            # increase first nums[j] by one
            # if nums[j] + 1!= nums[j+1]
            j = 0
            while j < k and nums[j+1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1
        return output


res= Solution().combine_binary(4, 2)


class testSolution(unittest.TestCase):
    def test0(self):
        output = [[1, 2],
                  [1, 3],
                  [1, 4],
                  [2, 3],
                  [2, 4],
                  [3, 4]]
        self.assertAlmostEqual(Solution().combine_dfs(4, 2), output)
        self.assertAlmostEqual(Solution().combine_backtrack(4, 2), output)


if __name__ == '__main__':
    unittest.main()
