"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHN APLSIIG YIR"

"""
import timeit


class solution_1:
    def convert(self, s: str, numRows: int) -> str:
        # base case:
        n = len(s)
        if n == 0 or n == 1 or numRows == 1:
            return s

        cycle = 2 * numRows - 2
        s_list = []

        for i in range(numRows):
            for j in range(i, n, cycle):
                s_list.append(s[j])
                if i != 0 and i != numRows - 1 and j + cycle - 2 * i < n:
                    s_list.append(s[j + cycle - 2 * i])

        new_str = ''.join(s_list)

        return new_str


class solution_2:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        L = ['']* numRows
        index, step = 0, 1
        for x in s:
            L[index] += x

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        return ''.join(L)


def test():
    """Stupid test function"""
    L = [i for i in range(100)]


def main():


    s = "PAYPALISHIRING"
    test1 = solution_1().convert(s, 3)
    test2 = solution_1().convert("a", 3)
    test3 = solution_1().convert(s, 4)

    assert test1 == "PAHNAPLSIIGYIR"
    assert test2 == 'a'
    assert test3 == "PINALSIGYAHRPI"

    test1_2 = solution_2().convert(s, 3)
    test2_2 = solution_2().convert("a", 3)
    test3_2 = solution_2().convert(s, 4)

    assert test1_2 == "PAHNAPLSIIGYIR"
    assert test2_2 == 'a'
    assert test3_2 == "PINALSIGYAHRPI"



if __name__ == "__main__":
    import timeit
    main()
    print(timeit.timeit("test()", setup="from __main__ import test"))





