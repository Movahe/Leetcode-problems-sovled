"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Note 1:  # zip() function returns a zip object, which is an iterator of tuples
where the first item in each passed iterator is paired together, and then the
second item in each passed iterator are paired together etc.
If one tuple contains more items, these items are ignored:

Note 2: sort function sorts the string array in both alphabetically and length of a String.
Note! sort function doesn’t work as it inplace. 

Note 3: Break statement stops the loop in which the statement. Continue statement skips a single iteration in a loop.
Both of them can be used in a for or while loop.
"""


import unittest


class solution0:
    def longestCommonPrefix(self, strs):
        prefix = []
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return ''.join(prefix)


class solution1:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        short_str = min(strs, key = len)
        for i, ch in enumerate(short_str):
            for other in strs:
                if other[i] != ch:
                    return short_str[:i]
        return short_str


"""
Next solution use the fact that the max string has the longest or shortest common prefix with 
words that are not min or max. So, we can get accurate results through comparing max and min.
"""

class solution2:
    def longestCommonPrefix(self, strs):
        if not strs: return ""

        s1 = min(strs)
        s2 = max(strs)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1


class TestSolution0(unittest.TestCase):
    def test0(self):
        strs = ["flower", "flow", "flight"]
        output = 'fl'
        self.assertEqual(solution0().longestCommonPrefix(strs), output)

    def test1(self):
        strs = ["dog", "racecar", "car"]
        output = ""
        self.assertEqual(solution0().longestCommonPrefix(strs), output)


class TestSolution1(unittest.TestCase):
    def test0(self):
        strs = ["flower", "flow", "flight", "common"]
        output = ''
        self.assertEqual(solution1().longestCommonPrefix(strs), output)

    def test1(self):
        strs = ["dog", "racecar", "car"]
        output = ""
        self.assertEqual(solution1().longestCommonPrefix(strs), output)


class TestSolution2(unittest.TestCase):
    def test0(self):
        strs = ["flower", "flow", "flight"]
        output = 'fl'
        self.assertEqual(solution2().longestCommonPrefix(strs), output)

    def test1(self):
        strs = ["dog", "racecar", "car"]
        output = ""
        self.assertEqual(solution2().longestCommonPrefix(strs), output)


if __name__ == "__main__":
    unittest.main()




