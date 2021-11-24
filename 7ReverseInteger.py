"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Ex1:
Input: x = 123
Output: 321

Ex2:
Input: x = -123
Output: -321

Ex3:
Input: x = 120
Output: 21
"""


class solution_1:
    def reverse(self, x: int) -> int:
        Max = 2 ** 31

        if x >= Max - 1 or x < -Max:
            return 0

        if x < 0:

            rev = int('-' + str(-x)[::-1])              # or rev = int('-' + str(x)[1:][::-1])


        else:
            rev = int(str(x)[::-1])

        if rev < -Max or rev >= Max - 1:

            rev = 0
        return rev


class solution_2:
    def reverse(self, x:int) ->int:
        Max = 2 ** 31
        res = str(abs(x))
        res = int(res[::-1])

        return (res if x >= 0 else 0 - res) if - Max <= res < Max - 1 else 0


def main():

    test1_1 = solution_1().reverse(-320)

    assert test1_1 == -23

    test1_2 = solution_2().reverse(-1)

    assert test1_2 == -1

    test2_2 = solution_2().reverse(-320)

    assert test2_2 == -23


if __name__ == "__main__":
    main()