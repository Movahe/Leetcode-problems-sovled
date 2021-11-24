import unittest

"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together 
the nodes of the first two lists.

Ex1: Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class solution:
    """
    l1, l2 are two sored linked lists.
    Argument: Merge two sorted linkd lists
    Return: sorted list
    """
    def mergeTwoLists1(self, l1, l2):
        dummy = cur = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next

            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2  # cur.next = l1 if l1 else l2
        return dummy.next

    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:  # if l1 is not empty, then it will return nothing. If l1 is empty, then return None.
            return l1 or l2

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2

