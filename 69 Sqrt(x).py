"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""
import unittest
import math


class solution0:
    def mySqrt_math(self, x: int) -> int:
        if x < 2:
            return x
        left = int(math.exp(0.5*math.log(x)))
        right = left + 1
        return left if right * right > x else right

    # Complexity Analysis
    #
    # Time complexity : O(1).
    #
    # Space complexity : O(1).

    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        i = 1
        res = 1
        while res <= x:
            i += 1
            res = i * i
        return i - 1


class solution1:
    def mySqrt(self, x: int) -> int:  # Binary search
        # For x >= 2, the square root is always smaller than x/2 and larger than 0 : 0 < a < x/2.
        if x < 2:
            return x
        l, r = 2, x//2
        while l <= r:
            mid = l + (r-l)//2
            num = mid*mid
            if num > x:
                r = mid - 1
            elif num < x:
                l = mid + 1
            else:
                return mid
        return r

    # Time complexity: O(log N)
    # T(N) = aT(N/b) + f(N^d), a = 1, b = 2, d=0, log_b a=d
    # critical = log_b a = log(# sub-problems)/log(relative sub-problem size.)
    # hence dealing with case 2 result in O(n^(log_b a)log^(d+1)N )
    # Space complexity: O(1)

    # Case 1: f(N^d log^k n) is the work to split/recombine a sub_problem. when d < critical
    # upper bounded by a lesser exponent polynomial. ~~~
    # T(N) = O(n^{log_b a})

    # Case 2: d = log_b a, T(N) = O(n^d log^(k+1) N)

    # Case 3: d > log_b a, T(N) = O(n^d)


class Testsolution0(unittest.TestCase):
    def test0(self):
        x = 4
        out = 2
        self.assertEqual(solution0().mySqrt(x), out)

    def test1(self):
        x = 8
        out = 2
        self.assertEqual(solution0().mySqrt(x), out)

    def test2(self):
        x = 90
        out = 9
        self.assertEqual(solution0().mySqrt(x), out)


class Testsolution1(unittest.TestCase):
    def test0(self):
        x = 4
        out = 2
        self.assertEqual(solution1().mySqrt(x), out)

    def test1(self):
        x = 8
        out = 2
        self.assertEqual(solution1().mySqrt(x), out)

    def test2(self):
        x = 90
        out = 9
        self.assertEqual(solution1().mySqrt(x), out)

if __name__ == "__main__":
    unittest.main()