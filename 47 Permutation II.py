"""
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.
"""
from collections import Counter


class Solution_dfs:
    def permuteUnique(self, nums: list) -> list:
        res = []
        nums.sort()  # sort is needed to put all the same element in consecutive, then we can pass these duplicates.
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, comb, res):
        if not nums:
            res.append(comb)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  # to skip the duplicate.
                continue
            self.dfs(nums[:i] + nums[i+1:], comb + [nums[i]], res)


class Solution_backtracking:
    def permuteUnique(self, nums: list) -> list:
        res = []

        def backtracking(nums, counter, comb):
            if len(comb) == len(nums):
                res.append(list(comb))
                return
            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtracking(nums, counter, comb)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1
        backtracking(nums, Counter(nums), [])

        return res


nums = [1, 1, 3]
output = Solution_dfs().permuteUnique(nums)
print(output)
assert output == [[1, 1, 3], [1, 3, 1], [3, 1, 1]]
output1 = Solution_backtracking().permuteUnique(nums)
print(output1)
assert output1 == [[1, 1, 3], [1, 3, 1], [3, 1, 1]]


