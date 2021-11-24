class solution_1:
    def myAtoi(self, s:str)->int:

        s = s.strip()
        res = ''
        flag = False
        max_int = 2**31 - 1
        min_int = - 2**31
        for i in range(len(s)):
            if s[i].isdigit() or s[i] in ('+', '-'):
                if flag:
                    if s[i] in ('+', '-'):
                        break
                flag = True
                res += s[i]
            else:
                break

        if not flag:
            return 0

        if len(res) == 1:
            if res in ('+', '-'):
                return 0
            else:
                return int(res)

        if min_int <= int(res) <= max_int:
            return int(res)

        elif int(res) < min_int:
            return min_int
        elif int(res) > max_int:
            return max_int


class solution_2:
    def myAtoi(self, s:str) -> int:
        s = s.strip()
        res = ''
        sign = 1
        max_int = 2**31 - 1
        min_int = - 2**31
        if len(s) == 0:
            return 0
        sign = -1 if s[0] == '-' else 1

        res = 0
        i = 1 if s[0] in '+-' else 0
        while i < len(s) and s[i].isdigit():
            res = res*10 + int(s[i])
            i +=1

        return max( min_int, min(sign*res, max_int))






def main():
    test1 = solution_1().myAtoi("42")
    test2 = solution_1().myAtoi("   -42")
    test3 = solution_1().myAtoi("4193 with words")
    test4 = solution_1().myAtoi("words and 987")
    test5 = solution_1().myAtoi("-91283472332")
    assert test1 == 42
    assert test2 == -42
    assert test3 == 4193
    assert test4 == 0
    assert test5 == -2147483648

    test1_2 = solution_2().myAtoi("42")
    test2_2 = solution_1().myAtoi("   -42")
    test3_2 = solution_1().myAtoi("4193 with words")
    test4_2 = solution_1().myAtoi("words and 987")
    test5_2 = solution_1().myAtoi("-91283472332")
    assert test1_2 == 42
    assert test2_2 == -42   
    assert test3_2 == 4193
    assert test4_2 == 0
    assert test5_2 == -2147483648


if __name__ == "__main__":
    main()
