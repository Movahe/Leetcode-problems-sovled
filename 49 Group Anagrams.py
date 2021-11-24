"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""
from collections import defaultdict
import unittest


class Solution:
    def groupAnagrams(self, strs: str):
        res = defaultdict(list)
        for s in strs:
            temp = list(s)
            temp.sort()
            res[tuple(temp)].append(s)
        return list(res.values())

    # Time complexity: O(NKlogK), N is the length of strs K is the
    #                   maximum length of a string in strs. The outer loop has complexity
    #                   O(N) as we iterate through each string. sort each string in O(KlogK) time.)
    # Space complexity: O(NK), the total information stored in ans.

    def groupAnagrams1(self, strs: str):
        ans = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] +=1
            ans[tuple(count)].append(s)
        return list(ans.values())

    # time complexity: O(NK), N is the length of strs K is the
    #                  maximum length of a string in strs. Counting each string is linear in
    #                  the size of the string, and we count every string.
    # Space complexity: O(NK)


class testSolution(unittest.TestCase):
    def test0(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        output = [["eat","tea","ate"],["tan","nat"],["bat"]]
        self.assertEqual(Solution().groupAnagrams(strs), output)
        self.assertEqual(Solution().groupAnagrams1(strs), output)



if __name__ == '__main__':
    unittest.main()