"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
"""
import unittest


class Solution:
    def countAndSay0(self, n):
        """
        :type n: int
        :return: str
        """
        if n == 1:
            return '1'

        prev = '1'
        res = ''
        for i in range(1, n):
            count = 1
            for j in range(len(prev) - 1):
                if prev[j] == prev[j+1]:
                    count += 1
                else:
                    res += str(count) + prev[j]
                    count = 1
            res += str(count) + prev[-1]
            prev = res
            res = ''
        return prev

    def countAndSay(self, n):
        if n == 1:
            return '1'

        s = self.countAndSay(n-1)
        res = ''
        cnt = 1
        i = 1
        while i < len(s) + 1:
            if i < len(s) and s[i] == s[i-1]:
                cnt += 1

            else:
                res += str(cnt) + str(s[i-1])
                cnt =1

            i += 1
        return res


class testSolution(unittest.TestCase):
    def test0(self):
        n = 2
        output = '11'
        self.assertEqual(Solution().countAndSay0(n), output)
        self.assertEqual(Solution().countAndSay(n), output)

    def test1(self):
        n = 3
        output = '21'
        self.assertEqual(Solution().countAndSay0(n), output)
        self.assertEqual(Solution().countAndSay(n), output)

    def test2(self):
        n = 5
        output = '111221'
        self.assertEqual(Solution().countAndSay0(n), output)
        self.assertEqual(Solution().countAndSay(n), output)


if __name__ == "__main__":
    unittest.main()








