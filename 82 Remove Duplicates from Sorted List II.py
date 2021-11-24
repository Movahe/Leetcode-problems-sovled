"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Ex1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Ex2:
Input: head = [1,1,1,2,3]
Output: [2,3]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # sentinel
        sentinel = ListNode(0, head)

        # predecessor = the last node before the sublist of duplicates
        pred = sentinel

        while head:
            # if it's a beginning of duplicates sublist
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next

                # skip all duplicates
                pred.next = head.next

            # otherwise, move predecessor
            else:
                pred = pred.next

            # move forward
            head = head.next

        return sentinel.next

    def deleteDuplicates_recursive(self, head: "ListNode") -> ListNode:
        if not head or head.next:
            return head

        if head.val == head.next.val:
            # skip duplicate nodes
            while head.next and head.val == head.next.val:
                head = head.next

                return self.deleteDuplicates_recursive(head.next)
        else:
            head.next = self.deleteDuplicates_recursive(head.next)
            return head



