"""
Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
Author: Youngsoo Lee
Time complexity: O(n)
"""
import sys
sys.path.insert(0, '..') # hack for importing utils
from utils import ListNode, array2listnode, listnode2array


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

    def runAlgorithm(array, n):
        # Convert list to a linked list before passing the params.
        # After calling the solution function, re-convert the linked node value to a list value.
        return listnode2array(s.removeNthFromEnd(array2listnode(array), n))

    assert runAlgorithm([1,2,3,4,5], 2) == [1,2,3,5]
    assert runAlgorithm([1], 1) == []
    assert runAlgorithm([1, 2], 1) == [1]
    assert runAlgorithm([1, 2], 2) == [2]
