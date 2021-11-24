"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in
the string.

A word is a maximal substring consisting of non-space characters only.

Note:
str.isspace(): this function determines if the str contains only spaces
str.split(): could split the input string into several substrings, based on the give delimiter(by default, the delimiter
is space).

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # trim the trailing spaces in the end
        p = len(s) - 1
        while p >= 0 and s[p] == ' ':
            p -= 1

        # compute the length of last word
        word = ''
        count = 0
        while p >= 0 and s[p] != ' ':
            word += s[p]
            count += 1
            p -= 1
        return len(word)
        # return count

    # Time complexity: O(N)
    # Space complexity: O(N), if use count, that would be O(1)

    def lengthOfLastWord1(self, s: str) -> int:
        p, length = len(s), 0
        while p > 0:
            p -= 1

            # trim the trailing spaces in the end
            if s[p] != ' ':
                length += 1

            # the second time we meet " " gives us the last word
            elif s[p] == ' ' and length > 0:
                return length
        return length

    # one loop.     # Time complexity: O(N)
    #     # Space complexity: O(1)

    def lengthOfLastWord2(self, s: str) -> int:  # built in function
        return 0 if not s or s.isspace() else len(s.split()[-1])


s = "   fly me   to   the moon  "
res = Solution().lengthOfLastWord(s)
assert res == 4
res1 = Solution().lengthOfLastWord1(s)
assert res1 == 4
res2 = Solution().lengthOfLastWord2(s)
assert res2 == 4


