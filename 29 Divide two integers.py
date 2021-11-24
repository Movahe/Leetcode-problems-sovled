#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:38:59 2021
"""
import unittest


class solution0:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants.
        max_int, min_int = 2**31 - 1, - 2**31

        if dividend == min_int and divisor == -1:
            return max_int

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = - divisor

        res = 0
        while dividend - divisor <= 0:
            res -= 1
            dividend -= divisor

        return - res if negatives != 1 else res

"""
Time complexity: O(N)
Consider the worst case where the divisor is 1. For any dividend n, we'll need to subtract 
1 a total of n times to get to 0. Therefore, the time complexity is O(N) in the worst case.

Space Complexity : O(1)
We only use a fixed number of integer variables, so the space complexity is O(1)
"""
class solution1:
    def divide(self, dividend: int, divisor: int) -> int:

        max_int, min_int = 2**31 - 1, - 2**31
        half_min_int = -1073741824  # Min_int//2

        if dividend == min_int and divisor == -1:
            return max_int

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = - dividend
        if divisor > 0:
            negatives -= 1
            divisor = - divisor

        res = 0

        while dividend - divisor <= 0:
            powerOfTwo = -1
            value = divisor
            while value + value >= dividend and value >= half_min_int:
                value += value
                powerOfTwo += powerOfTwo

            res += powerOfTwo

            dividend -= value

        return -res if negatives != 1 else res

"""
Time complexity is: O(log^2 n)
Space complexity: O(1) Because only a constant number of single-value variables are used, 
the space complexity is O(1).
"""


class solution2:
    def divide(self, dividend: int, divisor: int) -> int:
        min_int, max_int = -2**31, 2**31 -1
        half_min_int = -2**30

        if dividend == min_int and divisor == -1:
            return max_int

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        doubles = []
        powers = []

        # Nothing too exciting here, we're just making a list of doubles of 1 and
        # the divisor. This is pretty much the same as Approach 2, except we're
        # actually storing the values this time. */
        powersOfTwo = 1
        while dividend - divisor <= 0:
            doubles.append(divisor)
            powers.append(powersOfTwo)
            if divisor < half_min_int:
                break

            divisor += divisor
            powersOfTwo += powersOfTwo

        res = 0
        for i in reversed(range(len(doubles))):
            if doubles[i] >= dividend:
                res += powers[i]
                dividend -= doubles[i]
        return res if negatives != 1 else -res


class testSolution(unittest.TestCase):
    def test0(self):
        dividend = 214748364
        divisor = 3
        out = 71582788
        self.assertEqual(solution0().divide(dividend, divisor), out)
        self.assertEqual(solution1().divide(dividend, divisor), out)
        self.assertEqual(solution2().divide(dividend, divisor), out)


if __name__ == '__main__':
    unittest.main()


