"""
Given a string s, return the longest palindromic substring in s.

Ex1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Ex2:
Input: s = "cbbd"
Output: "bb"

Ex3:
Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"

"""

"""
solution1 use the brute force, 
step1: find all the substring of a given string, and check if there are the longestPalindrome, if so, then append to the list
step2: find the maximum length of a substring and return such a substring.

Time complexity: find all substring take O(n^2) and O(n) time to verify it.  Space comlexity: O(1)
"""
class solution1:
    def longestPalindrome(self, s: str) -> str:
        d = []
        max_length = 0
        max_string = ""
        for i in range(len(s)):
            for j in range(1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    L = len(s[i:j])
                    if L > max_length:
                        max_length = L
                        max_string = s[i:j]
        return max_string


"""
Using dynamic programming:
step1: Define a function, P(i,j) = True if s[i] = s[i:j] is Palindromic false otherwise:
Then P(i, j)=(P(i+1, j-1) and s[i] == s[j])
    Base cases are: P(i, i) = True   P(i, i+1) = (s[i]==s[i+1])
    
Time complexity: O(n^2), space complexity O(N^2)   

"""


class solution2:
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return s

        res = ""
        dp =[ [None for i in range(len(s))] for j in range(len(s))]

        for j in range(len(s)):
            for i in range(j+1):
                if i == j:
                    dp[j][i] = True
                elif j == i+1:
                    dp[j][i] = (s[i] == s[j])
                else:
                    dp[j][i] = (dp[j-1][i+1] and s[i] == s[j])

                if dp[j][i] and j - i + 1 > len(res):
                    res = s[i:j+1]

        return res


class solution2_a:
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return s
        res = ""
        dp = [None for i in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                if i == j:
                    dp[i] = True
                elif j == i+1:
                    dp[i] = (s[i] == s[j])
                else:
                    dp[i] = (dp[i+1] and s[i] == s[j])
                if dp[i] and j - i + 1 > len(res):
                    res = s[i:j+1]
        return res


"""
A Palindromic is symmetric around its centers, so try to expand around its 2n-1 centers, time complexity is O(n^2).
Space complexity : O(1)
"""


class solution_3:
    def longestPalindrome(self, s: str) -> str:
        self.maxlen = 0
        self.start = 0

        for i in range(len(s)):
            self.expandFromCenter(s, i, i)
            self.expandFromCenter(s, i, i + 1)
        return s[self.start: self.start + self.maxlen]

    def expandFromCenter(self, s, l, r):
        while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            if self.maxlen < r - l - 1:
                self.maxlen = r - l - 1
                self.start = l + 1


def main():
    test1_1 = solution1().longestPalindrome("babad")
    test2_1 = solution1().longestPalindrome("cbbd")
    test3_1 = solution1().longestPalindrome('a')
    test4_1 = solution1().longestPalindrome('ac')
    test5_1 = solution1().longestPalindrome('babad')

    assert test1_1 == 'bab'
    assert test2_1 == 'bb'
    assert test3_1 == 'a'
    assert test4_1 == 'a'
    assert test5_1 == 'bab'
    print("test functions passed for brutal force approach!")

    test1_2 = solution2().longestPalindrome("babad")
    test2_2 = solution2().longestPalindrome("cbbd")
    test3_2 = solution2().longestPalindrome('a')
    test4_2 = solution2().longestPalindrome('ac')
    test5_2 = solution2().longestPalindrome('babad')

    assert test1_2 == 'bab'
    assert test2_2 == 'bb'
    assert test3_2 == 'a'
    assert test4_2 == 'a'
    assert test5_2 == 'bab'

    print("test functions passed for dynamic approach!")


    test1_2a = solution2_a().longestPalindrome("babad")
    test2_2a = solution2_a().longestPalindrome("cbbd")
    test3_2a = solution2_a().longestPalindrome('a')
    test4_2a = solution2_a().longestPalindrome('ac')
    test5_2a = solution2_a().longestPalindrome('babad')

    assert test1_2a == 'bab'
    assert test2_2a == 'bb'
    assert test3_2a == 'a'
    assert test4_2a == 'a'
    assert test5_2a == 'bab'

    print("test functions passed for optimal dynamic approach!")


    test1_3 = solution_3().longestPalindrome("babad")
    test2_3 = solution_3().longestPalindrome("cbbd")
    test3_3 = solution_3().longestPalindrome('a')
    test4_3 = solution_3().longestPalindrome('ac')
    test5_3 = solution_3().longestPalindrome('babad')

    assert test1_3 == 'bab'
    assert test2_3 == 'bb'
    assert test3_3 == 'a'
    assert test4_3 == 'a'
    assert test5_3 == 'bab'

    print("test functions passed for expand from center approach!")



if __name__ == "__main__":
    main()
