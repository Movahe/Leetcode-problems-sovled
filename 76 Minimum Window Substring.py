"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
character in t (including duplicates) is included in the window. If there is no such substring,
return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""
import collections


class Solution:
    def minWindow_0(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        dict_t = collections.Counter(t)
        t_len = len(t)
        res = []
        l, r = 0, 0
        while l < len(s) - len(t)+1:
            temp = collections.Counter(t)
            print("temp:", temp)
            for r in range(l, len(s)):
                if s[r] in temp and temp[s[r]] > 0:
                    temp[s[r]] -= 1
                if all(v == 0 for v in temp.values()):
                    res.append(s[l:r + 1])
                    break
            l += 1

        print(res)

        len_res = [len(x) for x in res]
        print(len_res)
        return '' if res == [] else res[len_res.index(min(len_res))]

    def minWindow(self, s: str, t: str) -> str:

        # hash table to store the required char frequency
        need = collections.Counter(t)

        # total character count we need to care about
        missing = len(t)

        # windowStart and windowEnd to be
        windowStart, windowEnd = 0, 0
        i = 0

        # iterate over s starting over index 1
        for j, char in enumerate(s, 1):

            # if char is required then decrease missing
            if need[char] > 0:
                missing -= 1

            # decrease the freq of char from need (maybe be negative - which basically denotes
            #   that we have few extra characters which are not required but present in between current window)
            need[char] -= 1

            print("need:", need)

            # we found a valid window
            if missing == 0:
                # chars from start to find the real windowStart
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1

                # if it's only one char case or curr window is smaller, then update window
                if windowEnd == 0 or j - i < windowEnd - windowStart:
                    windowStart, windowEnd = i, j

                # now resetting the window to make it invalid
                # sure the first appearing char satisfies need[char]>0
                need[s[i]] += 1

                # missed this first char, so add missing by 1
                missing += 1

                # update i to windowStart+1 for next window
                i += 1

        return s[windowStart:windowEnd]


s = "ADOBECODEBANC"
t = "ABC"

s1 = 'a'
t1 = 'aa'
res = Solution().minWindow(s, t)
print(res)

