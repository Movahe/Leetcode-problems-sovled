"""

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth
characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does
not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Ex1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :param words:  List[str]
        :param maxWidth: int
        :return:  List[str]
        """
        result, current_list, num_of_letters = [], [], 0
        # result -> stores final result output
        # current_list -> stores list of words which are traversed but not yet added to result
        # num_of_letters -> stores number of chars corresponding to words in current_list

        for word in words:

            # total no. of chars in current_list + total no. of chars in current word
            # + total no. of words ~= min. number of spaces between words
            if num_of_letters + len(word) + len(current_list) > maxWidth:
                # size will be used for module "magic" for round robin
                # we use max. 1 because at least one word would be there and to avoid modulo by 0
                size = max(1, len(current_list)-1)

                for i in range(maxWidth-num_of_letters):
                    index = i%size
                    current_list[index] += ' '

                # add current line of words to the output
                result.append("".join(current_list))

                current_list, num_of_letters = [], 0

            # add current word to the list and add length to char count
            current_list.append(word)
            num_of_letters += len(word)

        # from last line by join with space and left justify to maxWidth using ljust(python method)
        # that means pad additional spaces to the right to make string length equal to maxWidth
        result.append(' '.join(current_list).ljust(maxWidth))

        return result


words = ["This", "is", "an", "example", "of", "text", "justification."]
words1 = ["What", "kinds", "of", "acknowledgment", "shall", "be", "written?"]
maxWidth = 16
res = Solution().fullJustify(words1, maxWidth)
for i in res:
    print(i)


