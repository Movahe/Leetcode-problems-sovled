"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Ex1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Ex2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
import copy
import unittest


class solution1:
    def climbStairs(self, n: int) -> int:
        steps = {"1": 1, "2": 2}
        for i in range(3, n + 1):
            steps[str(i)] = steps[str(i - 1)] + steps[str(i - 2)]

        return steps[str(n)]


class solution2:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        else:
            steps = [1, 2]
            for i in range(3, n+1):
                temp = steps[-1] + steps[-2]
                steps.append(temp)
            return steps[-1]


class solution3:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        else:
            steps = [1, 2]
            for i in range(3, n+1):
                temp = copy.copy(steps)
                next = temp.pop() + temp.pop()
                steps.append(next)
            return steps[-1]

    def climbStairs_dp(self, n:int) -> int:
        if n == 1 or n == 2:
            return n
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

    # Complexity Analysis
    #
    # Time complexity : O(n). Single loop upto n.
    #
    # Space complexity : O(n). dp array of size n is used.


class Testsolution1(unittest.TestCase):
    def test0(self):
        nums = 3
        output = 3
        self.assertEqual(solution1().climbStairs(nums), output)
        self.assertEqual(solution2().climbStairs(nums), output)
        self.assertEqual(solution3().climbStairs(nums), output)
        self.assertEqual(solution3().climbStairs_dp(nums), output)


if __name__ == "__main__":
    unittest.main()