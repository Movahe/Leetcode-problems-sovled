"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not

Ex1:
Input: x = 121
Output: true

Ex2:
Input: x = -121
Output: false

Ex3:
Input: x = 10
Output: false

Ex4:
Input: x = -101
Output: false

Ex5:
Input: x = 0
Output: True

"""

import math
import numpy as np


class solution_1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False

        else:
            return True if x == int(str(x)[::-1]) else False


class solution_2:
    def isPalindrome(self, x: int) ->bool:
        return str(x) == str(x)[::-1]


class solution_3:
    def isPalindrome(self, x: int) ->bool:
        if x < 0:
            return False

        x_copy = x
        res = 0
        while x > 0:
            res = res*10 + x % 10
            x = x // 10

        return x_copy == res






def main():

    tests = [121, -121, 10, -101, 0, 2346]
    test_outputs = [True, False, False, False, True, False]
    for i, test in enumerate(tests):
        assert solution_1().isPalindrome(test) == test_outputs[i]
        assert solution_2().isPalindrome(test) == test_outputs[i]
        assert solution_3().isPalindrome(test) == test_outputs[i]

    print("Passed all the tests!")


if __name__ == "__main__":
    main()