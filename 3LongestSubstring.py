"""
Given a string s, find the length of the longest substring without repeating characters.

Ex1:Input: s = "abcabcbb"   Output: 3
    Explanation: The answer is "abc", with the length of 3.

Ex2:Input: s = "bbbbb"      Output: 1
    Explanation: The answer is "b", with the length of 1.

Ex3:Input: s = "pwwkew"     Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Ex4:Input: s = ""           Output: 0
"""


def lengthOfLongestSubstring(s):
    """
    :type s: str               : The ord() function: returns an integer representing the Unicode character.
    :rtype: int                : print(ord('5'))    # 53
    """
    chars = [0] * 128
    left = right = 0

    res = 0
    while right < len(s):
        r = s[right]
        chars[ord(r)] += 1
        while chars[ord(r)] > 1:
            l = s[left]
            chars[ord(l)] -= 1
            left += 1

        res = max(res, right - left + 1)

        right += 1
    return res


def lengthOfLongestSubstring_2(s):
    start = max_length = 0
    used = {}
    for i, s_ in enumerate(s):
        if s_ in used and start <= used[s_]:
            start = used[s_] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used[s_] = i

    return max_length


A = lengthOfLongestSubstring('abcdeabifgh')

B = lengthOfLongestSubstring_2('abcdeabifgh')

C = lengthOfLongestSubstring_2("pwwkew")
D = lengthOfLongestSubstring("pwwkew")


assert A == B == 9

assert C == D == 3