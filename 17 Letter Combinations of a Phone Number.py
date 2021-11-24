import unittest


"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent. Return the answer in any order.
"""


class solution0:  # using the recursive calls
    def letterCombinations(self, digits):

        k_maps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                  '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(k_maps[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = k_maps[digits[-1]]
        return [s + c for s in prev for c in additional]


class solution1:
    def letterCombinations(self, digits):

        k_maps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                  '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = ['']
        for d in digits:
            res = [prev + cur for prev in res for cur in k_maps[d]]
        return res if len(digits) > 0 else []


class solution2:  # DFS search
    def letterCombinations(self, digits):

        k_maps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                  '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        res = []
        if len(digits) == 0:
            return res

        self.dfs(digits, 0, k_maps, '', res)
        return res

    def dfs(self, digits, index, k_maps, path, res):
        if index >= len(digits):
            res.append(path)
            return
        string1 = k_maps[digits[index]]
        for i in string1:
            self.dfs(digits, index+1, k_maps, path+i, res)



class TestSolution0(unittest.TestCase):
    def test0(self):
        digits = '23'
        out = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(solution0().letterCombinations(digits), out)

    def test1(self):
        digits = '2'
        out = ["a", "b", "c"]
        self.assertEqual(solution0().letterCombinations(digits), out)

    def test2(self):
        digits = '234'
        out = ["adg", "adh", "adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
        self.assertEqual(solution0().letterCombinations(digits), out)


class TestSolution1(unittest.TestCase):
    def test0(self):
        digits = '23'
        out = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(solution1().letterCombinations(digits), out)

    def test1(self):
        digits = '2'
        out = ["a", "b", "c"]
        self.assertEqual(solution1().letterCombinations(digits), out)

    def test2(self):
        digits = '234'
        out = ["adg", "adh", "adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
        self.assertEqual(solution1().letterCombinations(digits), out)


class TestSolution2(unittest.TestCase):
    def test0(self):
        digits = '23'
        out = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(solution2().letterCombinations(digits), out)

    def test1(self):
        digits = '2'
        out = ["a", "b", "c"]
        self.assertEqual(solution2().letterCombinations(digits), out)

    def test2(self):
        digits = '234'
        out = ["adg", "adh", "adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
        self.assertEqual(solution2().letterCombinations(digits), out)


if __name__ == '__main__':
    unittest.main()