"""
A valid number can be split up into these components (in order):

1). A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.

2) An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7",
"+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers:
["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot = False
        for i, c in enumerate(s):
            # If the character is a digit, set seenDigit = true.
            if c.isdigit():
                seen_digit = True

            # If the character is a sign, check if it is either the first character of the input,
            # or if the character before it is an exponent. If not, return false
            elif c in ["+", "-"]:
                if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False

            # If the character is an exponent, first check if we have already seen an exponent
            # or if we have not yet seen a digit. If either is true, then return false.
            elif c in ["e", "E"]:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # We need to reset seenDigit because after an exponent, we must construct a new integer.
                seen_digit = False
            # If the character is a dot, first check if we have already seen either a dot or an exponent.
            # If so, return false. Otherwise, set seenDot = true.
            elif c == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            # If the character is anything else, return false.
            else:
                return False
        # At the end, return seenDigit. This is one reason why we have to reset seenDigit after seeing an exponent
        # - otherwise an input like "21e" would be incorrectly judged as valid.
        return seen_digit

    # Time complexity: O(N), N is the length of s
    # Space complexity: O(1). only store 3 variables.


    # Deterministic Finite Automaton(DFA)
    # A DFA is a finite number of states, with transition rules to move between them.

    def isNumber_DFA(self, s):
        # DFA we have designed
        dfa = [
            {'digit': 1, 'sign': 2, 'dot': 3},
            {'digit': 1, 'dot': 4, 'exponent': 5},
            {'digit': 1, 'dot': 3},
            {'digit': 4},
            {'digit': 4, 'exponent': 5},
            {'sign': 6, 'digit': 7},
            {'digit': 7},
            {'digit': 7}
        ]

        current_state = 0
        for c in s:
            if c.isdigit():
                group = 'digit'
            elif c in ['+', '-']:
                group = 'sign'
            elif c in ['e', 'E']:
                group = 'exponent'
            elif c == '.':
                group = 'dot'
            else:
                return False

            if group not in dfa[current_state]:
                return False
            current_state = dfa[current_state][group]

        return current_state in [1, 4, 7]

    # Time complexity:O(N), where N is the length of s.
    #
    # We simply iterate through the input once. The number of operations we perform for each character in the input
    # is independent of the length of the string, and therefore each operation requires constant time.
    # So we get N* O(1) = O(N), N⋅O(1)=O(N).
    #
    # Space complexity: O(1).
    #
    # We will construct the same DFA regardless of the input size.

