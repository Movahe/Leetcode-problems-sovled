"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Ex1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)

        # if one of the strings is empty
        if n * m == 0:
            return n + m
        # edit distance d[i][j] which is an edit distance between the first i characters of
        #  word1 and the first j characters of word2.
        # array to store the convention history
        d = [[0] * (m + 1) for _ in range(n + 1)]

        # init boundaries
        for i in range(n + 1):
            d[i][0] = i
        for j in range(m + 1):
            d[0][j] = j

        # DP compute
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = d[i - 1][j] + 1
                down = d[i][j - 1] + 1
                left_down = d[i - 1][j - 1]

                # If the last character is the same, i.e. word1[i] = word2[j] then
                # D[i][j]=1+min(D[i−1][j],D[i][j−1],D[i−1][j−1]−1)

                # If word1[i] != word2[j] we have to take into account the replacement of the last character
                # during the conversion.
                # D[i][j] = 1+min(D[i−1][j],D[i][j−1],D[i−1][j−1])
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                d[i][j] = min(left, down, left_down)
        # for dp in d:
        #     print(dp)
        return d[n][m]

    # Time complexity: O(m*n)
    # Space complexity: O(m*n)


word1 = "intention"
word2 = "execution"
res = Solution().minDistance(word1, word2)
assert res == 5