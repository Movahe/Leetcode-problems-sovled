"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer
does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

ex1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""


class Solution:
    def plusOne(self, digits):
        """
        :param digits: List[int]
        :return:  List[int]
        """
        carry = 1
        for i in reversed(range(len(digits))):
            carry, digits[i] = divmod(digits[i] + carry, 10)

        if carry > 0:
            return [carry] + digits
        else:
            return digits

        # Let NN be the number of elements in the input list.

        # Time complexity: O(N) since it's not more than one pass along the input list.

        # Space complexity: O(N) Although we perform the operation in-place (i.e. on the input list itself), in the
        # worst scenario, we would need to allocate an intermediate space to hold the result, which contains the N+1N+1
        # elements. Hence the overall space complexity of the algorithm is \mathcal{O}(N)O(N).


nums = [9, 9, 9]
res = Solution().plusOne(nums)
assert res == [1, 0, 0, 0]