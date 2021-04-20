"""
Problem: https://leetcode.com/problems/merge-two-sorted-lists/
Author: Youngsoo Lee
Time complexity: O(n)
"""
import sys
sys.path.insert(0, '..') # hack for importing utils
from utils import ListNode, array2listnode, listnode2array


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        empty_head = ListNode(-101) # Using -101 since -100 <= Node.val <= 100
        tail = empty_head

        while l1 or l2:
            if l2 is None or (l1 is not None and l1.val < l2.val):
                tail.next = l1
                l1 = l1.next
            elif l2 is not None:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        return empty_head.next


if __name__ == '__main__':
    s = Solution()

    def runAlgorithm(l1, l2):
        return listnode2array(s.mergeTwoLists(array2listnode(l1), array2listnode(l2)))

    assert runAlgorithm([1,2,4], [1,3,4]) == [1,1,2,3,4,4]
    assert runAlgorithm([], []) == []
    assert runAlgorithm([], [0]) == [0]
