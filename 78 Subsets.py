"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

"""
note: 
Permutation: N!
Combinations: N!/((N-k)!k!)
Subset: 2**N
Ways to deal with:Recursion, Backtracking. Lexicographic generation based on the mapping between binary 
bitmasks and the corresponding permutations / combinations / subsets.

"""

class Solution:  # Recursion/Cascading
    def subsets(self, nums: list) -> list:
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output
    # 1. Start from emtpy subset output = []
    # 2. Take 1 into consideration and add new subset by updating the existing ones.
    #       output = [[], [1] ]
    # 3. Take 2 into consideration and add new subset by updating the existing ones.
    #       output= [[], [1], [2], [1, 2]  ]
    # 4. Take 3 into consideration and add new subset by updating the existing ones.
    #       output= [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]  ]
    # And so on so forth

    # Time complexity: O(N * 2^N) to generate all the subsets and then copy them into output list
    # space complexity: O(N* 2^N)

    def subsets_recursive(self, nums: list) -> list:
        res = [[]]

        if not nums:
            return res

        for num in nums:
            for idx in range(len(res)):
                res.append(res[idx] + [num])
        return res


class Solution_BFS:
    def subsets(self, nums: list) -> list:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, comb, res):
        res.append(comb)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], comb+[nums[i]], res)


class Solution_backtacking:
    def subsets(self, nums: list) -> list:
        def backtrack(first=0, k=0, path=[], output=[]):
            if k == 0:
                output.append(path[:])
                return
            for i in range(first, len(nums)):
                path.append(nums[i])
                backtrack(i+1, k-1, path, output)
                path.pop()
        output = []
        for k in range(len(nums)+1):
            backtrack(0, k, [], output)
        return output


def main():
    nums = [1, 2, 3]
    res = Solution().subsets_recursive(nums)
    res1 = Solution_BFS().subsets(nums)
    res2 = Solution_backtacking().subsets(nums)
    print("subsets from backtracking:", res2)
    print(res1)
    output = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert res == output


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