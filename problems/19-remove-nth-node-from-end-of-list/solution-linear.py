"""
Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
Author: Youngsoo Lee
Time complexity: O(n)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node, target_node = head, head
        gap = 0

        while node.next:
            if gap == n:
                target_node = target_node.next
            else:
                gap += 1

            node = node.next

        if gap < n:
            head = head.next
        elif target_node.next:
            target_node.next = target_node.next.next

        return head

if __name__ == '__main__':
    s = Solution()

    def a2ll(array):
        # Array to link list
        head = ListNode(array[0])
        tail = head

        for i in range(1, len(array)):
            tail.next = ListNode(array[i])
            tail = tail.next

        return head

    def runAlgorithm(array, n):
        # Convert list to a linked list before passing the params.
        # After calling the solution function, re-convert the linked node value to a list value.
        node = s.removeNthFromEnd(a2ll(array), n)
        ret = []
        while node:
            ret.append(node.val)
            node = node.next
        print(ret)
        return ret

    assert runAlgorithm([1,2,3,4,5], 2) == [1,2,3,5]
    assert runAlgorithm([1], 1) == []
    assert runAlgorithm([1, 2], 1) == [1]
    assert runAlgorithm([1, 2], 2) == [2]
