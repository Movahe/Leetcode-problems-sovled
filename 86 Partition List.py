"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater
than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Ex1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Ex2:
Input: head = [2,1], x = 2
Output: [1,2]
"""
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x: int) :
        """
        :param head: Optional[ListNode]
        :param x: int
        :return: Optional[ListNode]
        """

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.

        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        while head:
            # If the original list node is lesser than the given x, assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next

            # If the original list node is greater than the given x, assign it to the after list.

            else:
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # For the bigger list, it should end with 5, but there is still 2 as its next, should set 5's next to none
        after.next = None
        before.next = after_head.next
        return before_head.next

    # Complexity Analysis
    # Time Complexity: O(N), where N is the number of nodes in the original linked list and
    # we iterate the original list.
    # Space Complexity: O(1), we have not utilized any extra space, the point to note is that we are reforming the
    # original list, by moving the original nodes, we have not used any extra space as such.