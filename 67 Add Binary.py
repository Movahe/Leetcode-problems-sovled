"""
Given two binary strings a and b, return their sum as a binary string.

Ex1:
Input: a = "11", b = "1"
Output: "100"

Ex2:
Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #“{:b}” is for converting the argument to a binary form
        return '{0:b}'.format(int(a, 2) + int(b, 2))

    # The overall algorithm has O(N+M) time complexity and has two drawbacks which could be used
    # against you during the interview.

    def addBinary_Bit_by_bit(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        carry = 0
        res = []
        for i in reversed(range(n)):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            if carry % 2 == 1:  # % remainder   1%2 = 1.  2%2=0, 0%2=0
                res.append('1')
            else:
                res.append('0')
            carry //= 2  # floor division. 0//2=0, 1//2=0. 2//2 =1
        if carry == 1:
            res.append('1')
        res.reverse()
        return ''.join(res)

    # Complexity Analysis
    # Time complexity: O(max(N,M)), where N and M are lengths of the input strings a and b.
    #
    # Space complexity: O(max(N, M)) to keep the answer.


    #Bit manipulation
    #           a = 1 1 1 1
    #           b = 0 0 1 0
    #      a XOR b= 1 1 0 1, a AND b = 0 0 1 0, then shit one bit to the left, (a&b)<<1 = 0 1 0 0 0
    #    a + b without the carry. a + b = (a XOR b) + (a AND b) << 1

    def addBinary_bit(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]  # removing "0b" prefix

        # bin(a), returns the binary string of a given integer a.
        # parameters: a: an integer to convert
        # return value: a binary string of an integer or int object
        # bin(4) = 0b100

        # Complexity Analysis
        #
        # Time complexity : O(N+M), where NN and MM are lengths of the input strings a and b.
        #
        # Space complexity : O(max(N,M)) to keep the answer

res = Solution().addBinary_bit(a='11', b='1')
print(res)