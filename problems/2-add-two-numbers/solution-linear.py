"""
Problem: https://leetcode.com/problems/add-two-numbers/
Author: Youngsoo Lee
Time complexity: O(max(n+m))
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        empty_head = ListNode()
        tail = empty_head
        carry = 0

        while l1 or l2:
            num = (l1.val if l1 else 0) + (l2.val if l2 else 0)

            if carry:
                num += 1
                carry = 0

            if num >= 10:
                carry = 1
                num -= 10

            tail.next = ListNode(num)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            tail.next = ListNode(carry)

        return empty_head.next


if __name__ == '__main__':
    s = Solution()
    
    def listToListNode(list_items):
        head = ListNode(list_items[0])
        tail = head

        for i in range(1, len(list_items)):
            tail.next = ListNode(list_items[i])
            tail = tail.next

        return head

    def runAlgorithm(l1, l2):
        # Convert list to a linked list before passing the params.
        # After calling the solution function, re-convert the linked node value to a list value.
        node = s.addTwoNumbers(listToListNode(l1), listToListNode(l2))
        ret = []
        while node:
            ret.append(node.val)
            node = node.next
        return ret

    assert runAlgorithm([2,4,3], [5,6,4]) == [7,0,8]
    assert runAlgorithm([0], [0]) == [0]
    assert runAlgorithm([9,9,9,9,9,9,9], [9,9,9,9]) == [8,9,9,9,0,0,0,1]
