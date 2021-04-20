"""
Problem: https://leetcode.com/problems/add-two-numbers/
Author: Youngsoo Lee
Time complexity: O(max(n+m))
"""
import sys
sys.path.insert(0, '..') # hack for importing utils
from utils import ListNode, array2listnode, listnode2array


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

    def runAlgorithm(l1, l2):
        # Convert list to a linked list before passing the params.
        # After calling the solution function, re-convert the linked node value to a list value.
        return listnode2array(s.addTwoNumbers(array2listnode(l1), array2listnode(l2)))

    assert runAlgorithm([2,4,3], [5,6,4]) == [7,0,8]
    assert runAlgorithm([0], [0]) == [0]
    assert runAlgorithm([9,9,9,9,9,9,9], [9,9,9,9]) == [8,9,9,9,0,0,0,1]
