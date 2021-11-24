"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of
the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
"""
import unittest


class Solution:

    # @lru_cache(maxsize=None)
    def recursiveWithMemo(self, index, s, memo) -> int:
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0

        if index == len(s) - 1:
            return 1

        # Memoization is needed since we might encounter the same sub-string.
        if index in memo:
            return memo[index]

        answer = self.recursiveWithMemo(index + 1, s, memo)
        if int(s[index: index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s, memo)

        memo[index] = answer
        return answer

    def numDecodings(self, s: str) -> int:
        memo = {}
        return self.recursiveWithMemo(0, s, memo)

    # Time complexity: O(N), where N is the length of the string.
    # Space complexity: O(N) The dictionary used for memoization would take the space equal to the length of the string.
    # There would be an entry for each index value. The recursion stack would also be equal to the length of the string.

    def numDecodings_DP(self, s: str) -> int:
        # Array to store the sub-problem results
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):

            # Check if successful single digit decode is possible.
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i - 2: i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]

    # Time Complexity: O(N), where N is length of the string. We iterate the length of dp array which is N+1.
    # Space Complexity: O(N). The length of the DP array.

    def numDecodings_1(self, s: str) -> int:
        if s[0] == '0':
            return 0
        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != '0':
                current = one_back
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += two_back
            two_back = one_back
            one_back = current

        return one_back
    # Time Complexity: O(N), where N is length of the string. We iterate the length of dp array which is N+1.
    # Space Complexity: O(1).


class testSolution(unittest.TestCase):
    def test0(self):
        s = "13452023"
        res = 4
        self.assertAlmostEqual(Solution().numDecodings(s), res)
        self.assertAlmostEqual(Solution().numDecodings_DP(s), res)
        self.assertAlmostEqual(Solution().numDecodings_1(s), res)


if __name__ == "__main__":
    unittest.main()
