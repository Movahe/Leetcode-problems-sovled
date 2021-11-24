"""
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s)
in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

Ex1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

"""
from collections import Counter
from collections import defaultdict
import unittest


class solution:
    def findSubstring(self, s, words):
        """
        :type s:  str
        :type words: List[str]
        :rtype: List[int]
        """
        c = Counter(words)
        m = len(words)
        n = len(words[0])
        res = []

#       # Loop over word length
        for k in range(n):
            left = k
            subd = defaultdict(int)
            count = 0

#            #Loop over the string
            for j in range(k, len(s) - n+1, n):
                word = s[j:j+n]
                if word in c:
                    subd[word] += 1
                    count += 1
                    ##Shift the window as long as we have encountered more number of a word than is needed

                    while subd[word] > c[word]:
                        subd[s[left:left+n]] -= 1
                        left += n
                        count -= 1
                    if count == m:
                        res.append(left)

                #If is not a valid word then just skip over the current word (Don't worry about the middle characters
                ##outer loop will take care of it)

                else:
                    left = j + n
                    subd = defaultdict(int)
                    count = 0
        return res


class testSolution(unittest.TestCase):
    def test0(self):
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        output = [0, 9]
        self.assertEqual(solution().findSubstring(s, words), output)

    def test1(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]
        output = []
        self.assertEqual(solution().findSubstring(s, words), output)

    def test2(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar","foo","the"]
        output = [6, 9, 12]
        self.assertEqual(solution().findSubstring(s, words), output)


if __name__ == "__main__":
    unittest.main()



