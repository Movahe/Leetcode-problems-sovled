"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
"""

import unittest
import collections
import bisect


class solution0:
    def threeSum(self, nums):
        """
        :type nums:  List[int]
        :return: list[List[int]]
        """
        res = set()

        # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # 2. Create a separate set for negatives and positives for O(1) look-up times

        N, P = set(n), set(p)

        # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -num in N:
                    res.add((-1 * num, 0, num))

        # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0

        if len(z) >= 3:
            res.add((0, 0, 0))

        # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -(n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -(p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        return [list(i) for i in list(res)]


class solution1:
    def threeSum(self, nums):
        counter = collections.Counter(nums)
        nums = sorted(counter)
        ret = []
        for i, num in enumerate(nums):
            # case i. three numbers are the same - [0,0,0]
            if num == 0:
                if counter[num] >= 3:
                    ret.append([0, 0, 0])
            # case ii. two numbers are the same
            elif counter[num] >= 2 and -2 * num in counter:
                ret.append([num, num, -2 * num])
            # case iii. all three numbers are distinct

            # bisect_left: the leftmost boundary for searching would be the smallest element to
            # the right of i+1, that's why the value is set to opposite - nums[-1]
            # it also uses the fact that add the three positive values won;t give a zero sum.
            if num < 0:
                opposite = -num
                left = bisect.bisect_left(nums, opposite - nums[-1], i + 1)
                right = bisect.bisect_right(nums, opposite / 2, left)
                for a in nums[left:right]:
                    b = opposite - a
                    if b in counter and a!=b:
                        ret.append([num, a, b])
        return ret


class testsolution0(unittest.TestCase):
    def test0(self):
        nums = [-1, 0, 1, 2, -1, -4]
        output = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(solution0().threeSum(nums), output)

    def test1(self):
        nums = [-1, 1, 0]
        output = [[-1, 0, 1]]
        self.assertEqual(solution0().threeSum(nums), output)


class testsolution1(unittest.TestCase):
    def test0(self):
        nums = [-1, 0, 1, 2, -1, -4]
        output = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(solution1().threeSum(nums), output)

    def test1(self):
        nums = [-1, 1, 0]
        output = [[-1, 0, 1]]
        self.assertEqual(solution1().threeSum(nums), output)


if __name__ == '__main__':
    unittest.main()