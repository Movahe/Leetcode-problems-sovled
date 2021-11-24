""" Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
    Ex1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    Ex2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]
    Ex3:
    Input: nums = [1]
    Output: [[1]]
"""

"""Recursive call"""
import itertools
import unittest


class Solution_permute:
    def generate_permute(self, nums):

        def permutations(nums):
            if len(nums) == 1:
                return [nums[:]]
            else:
                X = []
                for i in range(len(nums)):
                    n = nums.pop(0)
                    L = permutations(nums)
                    for j in L:
                        j.append(n)
                    X.extend(L)
                    nums.append(n)
                return X

        return permutations(nums)


class Solution2:
    def permute(self, nums):
        res = []
        if len(nums) == 1:
            res.append(nums)
        else:
            for ele in self.permute(nums[1:]):
                for i in range(len(ele)+1):
                    temp = ele.copy()
                    temp.insert(i, nums[0])
                    res.append(temp)
        return res

    def permute2(self, nums):
        return itertools.permutations(nums, len(nums))


class Solution_DFS:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, comb, res):
        if not nums:
            res.append(comb)

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], comb + [nums[i]], res)


"""
Visualization of who above DFS algorithm works!

dfs(nums = [1, 2, 3] , path = [] , result = [] )
|____ dfs(nums = [2, 3] , path = [1] , result = [] )
|      |___dfs(nums = [3] , path = [1, 2] , result = [] )
|      |    |___dfs(nums = [] , path = [1, 2, 3] , result = [[1, 2, 3]] ) # added a new permutation(P) to the result(res)
|      |___dfs(nums = [2] , path = [1, 3] , result = [[1, 2, 3]] )
|           |___dfs(nums = [] , path = [1, 3, 2] , result = [[1, 2, 3], [1, 3, 2]] ) # added a new P to the res
|____ dfs(nums = [1, 3] , path = [2] , result = [[1, 2, 3], [1, 3, 2]] )
|      |___dfs(nums = [3] , path = [2, 1] , result = [[1, 2, 3], [1, 3, 2]] )
|      |    |___dfs(nums = [] , path = [2, 1, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] ) # added a new P to the res
|      |___dfs(nums = [1] , path = [2, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] )
|           |___dfs(nums = [] , path = [2, 3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] ) # added a new P to the res
|____ dfs(nums = [1, 2] , path = [3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
       |___dfs(nums = [2] , path = [3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
       |    |___dfs(nums = [] , path = [3, 1, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] ) # added a new P to the res
       |___dfs(nums = [1] , path = [3, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] )
            |___dfs(nums = [] , path = [3, 2, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] ) # added a new P to the res
"""


class Solution_backtracking:
    def permute(self, nums: list) -> list:
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place the i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]

                # use next integers to complete the permutations
                backtrack(first + 1)

                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output
    # Time Complexity: O(NxN!)
    # Space complexity: O(N!) one has to keep N! solutions.


def main():

    nums =[1, 2, 3]
    output1 = Solution_permute().generate_permute(nums)
    output2 = Solution2().permute(nums)
    output3 = Solution_DFS().permute(nums)
    output4 = Solution_backtracking().permute(nums)
    print("\noutput1:\n", output1)
    print("\noutput2:\n", output2)
    print("\noutput3:\n", output3)
    print("\noutput3:\n", output4)


if __name__ == "__main__":
    main()


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