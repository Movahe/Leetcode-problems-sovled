"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""
import itertools
import numpy as np


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Idea: Traverse all the linked lists and collect the values of the nodes into an array.
      Sort and iterate over this array to get the proper value of nodes.
      Create a new sorted linked list and extend it with the new nodes.
"""


class Solution:
    def mergeKLists(self, Lists):
        nodes = []
        head = point = ListNode(0)
        for l in Lists:
            while l:
                nodes.append(l.val)
                l = l.next
        print(nodes)

        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


L =[[1, 4, 5], [1, 3, 4], [2, 6]]
L1 = l1 = ListNode(0)
L2 = l2 = ListNode(0)
L3 = l3 = ListNode(0)
i = 1
for l in itertools.zip_longest(*L):
    print(l)
    l1.next = ListNode(l[0])
    l1 = l1.next
    l2.next = ListNode(l[1])
    l2 = l2.next
    l3.next = ListNode(l[2])
    l3 = l3.next

out = Solution().mergeKLists([L1, L2, L3])

while out:
    print(out.val)
    out = out.next


"""
Time complexity: O(NlogN) where N is the total number of nodes.
    Collecting all the values costs O(N)
    A stable sorting algorithm costs O(NlogN)
    iterating for creating the linked list costs O(N)

Space complexity: O(N)
    Sorting cost O(N) space.
    Creating a new linked list costs O(N) space 
"""
