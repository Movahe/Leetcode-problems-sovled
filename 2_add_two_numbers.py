"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Ex1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Ex2:
Input: l1 = [0], l2 = [0]
Output: [0]
Ex3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_Linked_list(i: int):
    temp = None
    for val in str(i):
        val = int(val)
        node = ListNode(val)
        node.next = temp
        temp = node
    return node


class Solution:
    def addTwoNumbers(l1, l2):

        def decode(n: ListNode):
            i = 1
            while n is not None:
                yield n.val * i
                i *= 10
                n = n.next

        def encode(i: int):
            temp = None
            for val in str(i):
                val = int(val)
                node = ListNode(val)
                node.next = temp
                temp = node
            return node


        i1 = sum(decode(l1))
        print("decode(l1", decode(l1))
        print(i1)
        i2 = sum(decode(l2))
        print(i2)

        return encode(i1 + i2)


class solution_2:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next




def main():

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    L1 = make_Linked_list(342)
    L2 = make_Linked_list(465)
    print("L1", L1)
    print("L1:", L1.val)
    print("L1 next:", L1.next.val)
    LL1 = L1.next
    print("LL1.next", LL1.next.val )

    sol = Solution.addTwoNumbers(L1, L2)
    print(sol.val)
    print(sol.next.val)
    sol_next = sol.next
    print(sol_next.next.val)

    sol2 = solution_2().addTwoNumbers(L1, L2)
    temp = sol2
    while temp:
        print(temp.val)
        temp = temp.next

    # temp = encode(342)
    # print(temp.val)
    # print(temp.next.val)
    # x = temp.next
    # print(x.next.val)


if __name__ == "__main__":
    main()