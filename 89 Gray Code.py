"""
An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.
"""
import unittest


class Solution:
    # @return a list of integers
    '''
    from up to down, then left to right

    0   1   11  110
            10  111
                101
                100

    start:      [0]
    i = 0:      [0, 1]
    i = 1:      [0, 1, 3, 2]
    i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
    '''

    def grayCode(self, n):
        results = [0]
        for i in range(n):
            results += [x + pow(2, i) for x in reversed(results)]
        print(results)
        return results

    def grayCode_trick(self, n: int):
        """

        :param n: int
        :return: List[int]
        """
        res = []
        for i in range(2**n):  # >> means right shift. 101 >>1 --> 10
            # print("i:", i, "i>>1: ", i>>1)
            res.append(i^(i >> 1))
        return res

    # Fisrt, we can explore the data and try to figure out the pattern.
    # For example, when n=3, results start from 000, we can XOR last number in results with X .
    # result[i+1] = X[i] ^ result[i]
    # Below we can figure out the pattern of X:
    # result          X                  Y
    # 0 0 0         0 0 1           0 0 1 (1)
    # 0 0 1         0 1 0           0 1 0 (2)
    # 0 1 1         0 0 1           0 1 1 (3)
    # 0 1 0         1 0 0           1 0 0 (4)
    # 1 1 0         0 0 1           1 0 1 (5)
    # 1 1 1         0 1 0           1 1 0 (6)
    # 1 0 1         0 0 1           1 1 1 (7)
    # 1 0 0

    # So the keypoint is to generate X sequence. Here is the trick, actually X is lowest
    # one-bit of Y (natural number set).
    # According to bit-manipulation, we can get lowest one-bit of number by
    # X = Y & -Y
    # ~Y which inverts all bits
    # ~Y = - Y - 1
    # - Y = ~Y + 1,
    # This give us an idea of what -Y looks like in bin
    # 0000000000000101 = Y
    # 1111111111111010 = ~Y
    # 1111111111111011 = ~Y + 1 = -Y
    #
    # 0000000000000001 = Y & -Y
    def grayCode_bit(self, n:int) -> "List[int]":
        res = [0]
        for i in range(1, 2**n):
            # print("i:", i, "-i:", -i, "i&-i:", i & -i)
            res.append(res[-1] ^ (i & -i))
        return res

class testSolution(unittest.TestCase):
    def test0(self):
        n = 3
        res = [0,1,3,2,6,7,5,4]
        self.assertAlmostEqual(Solution().grayCode_bit(n), res)
        self.assertAlmostEqual(Solution().grayCode(n), res)
        self.assertAlmostEqual(Solution().grayCode_trick(n), res)


if __name__ == '__main__':
    unittest.main()

