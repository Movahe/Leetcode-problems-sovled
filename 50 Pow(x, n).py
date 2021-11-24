"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Ex 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Ex 2:
Input: x = 2.10000, n = 3
Output: 9.26100
"""
class Solution:
    def myPow(self, x, n):
        """
        :param x:  float
        :param n:  int
        :return:  float
        """
        def fastPow(x, n):
            if n == 0:
                return 1.0
            half = fastPow(x, n/2)
            if n % 2 == 0:
                return half*half
            else:
                return x*half*half
        N = n
        if N < 0:
            x = 1/x
            N = -N
        return fastPow(x, N)

    # Time complexity: O(log N), each time, N is reduced by half, we need at most O(log N)
    # computations to get the result.
    # Space complexity: O(1), We only need two variables for the current product and the final result of x


    def myPow2(self, x, n):
        if n == 0:
            return 1

        if n == 1:
            return x

        elif n < 0:
            x = 1 / x
            n = -n
        power = x
        multiplications = 1
        while n - multiplications * 2 >= 0:
            power *= power
            multiplications *= 2
        return power * self.myPow2(x, n - multiplications)

    # Time complexity: O(log N)
    # Space complexity: O(1), We only need two variables for the current product and the final result of x


output = Solution().myPow2(-2, 5)
output1 = Solution().myPow2(2, 5)
assert output == -32
assert output1 == 32