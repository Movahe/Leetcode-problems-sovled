"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
import unittest

class solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        : Instead of really removing the nth node, just remove the nth value. then recursively determine
        the indexes (counting from back), then shift the values for all indexes larger than n, and then always drop the head.
        """

        def index(node):
            if not node:
                return 0

            i = index(node.next) + 1
            print("i:{}, node.val:{}".format(i, node.val))
            if i > n:
                node.next.val = node.val
            return i

        index(head)
        return head.next


class solution1:
    def removeNthFromEnd(self, head, n):
        def remove(head, n):
            if head == None:
                return head, 0

            node, count = remove(head.next, n)
            count += 1
            head.next = node

            if count == n:
                head = head.next
            return head, count

        return remove(head, n)[0]


class solution2:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l0 = ListNode(1)
l1 = ListNode(2)
l2 = ListNode(3)
l3 = ListNode(4)
l0.next = l1
l1.next = l2
l2.next = l3
so = solution1().removeNthFromEnd(l0, 2)

