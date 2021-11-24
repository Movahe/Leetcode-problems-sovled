"""

Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can
return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and
cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and
"0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
"""


class Solution:
    def restoreIpAddresses(self, s):
        """
        :param s: str
        :return: List[str]
        """

        def valid(segment):
            """
            Check if the current segment is valid:
            1. less or equal to 255
            2. the first character could be '0' only if the segment is equal to '0'
            """
            return int(segment) <=255 if segment[0] !='0' else len(segment) == 1

        def update_output(curr_pos):
            """
            Append the current list of segments to the list of solutions
            """
            segment = s[curr_pos+1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()

        def backtrack(prev_pos = -1, dots=3):
            """
            prev_pos: the position of the previously placed dot
            dots: number of dots to place
            """
            # The current dot curr_pos could be placed
            # in a range from prev_pos + 1 to prev_pos + 4.
            # The dot couldn't be placed after the last character in the string
            for curr_pos in range(prev_pos+1, min(n-1, prev_pos+4)):
                segment = s[prev_pos+1: curr_pos+1]
                if valid(segment):
                    segments.append(segment) # place dot
                    if dots - 1 == 0:  # if all 3 dots are placed
                        update_output(curr_pos)  # add the solution to output

                    else:
                        backtrack(curr_pos, dots-1)  # continue to place dots

                    segments.pop()  # remove the last placed dot

        n = len(s)
        output, segments = [], []
        backtrack()
        return output

    def restoreIpAddresses_backtrack(self, s):

        def backtrack(s, current, start, res):
            # if len(current) > 4:
            #     return
            if len(current) == 4:
                if start == len(s):
                    res.append('.'.join(current))
                return

            for i in range(start, min(start+3, len(s))):
                if i > start and s[start] == '0':
                    continue
                if 0 <= int(s[start:i+1]) <= 255:
                    backtrack(s, current+[s[start:i+1]], i+1, res)
                    print("current:", current)

        res = []
        backtrack(s, [], 0, res)
        return res



s = "010010"
res = Solution().restoreIpAddresses(s)
res2 = Solution().restoreIpAddresses_backtrack(s)
print(res)
assert res2 == ['0.10.0.10', '0.100.1.0']


