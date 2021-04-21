"""
Problem: https://leetcode.com/problems/swap-nodes-in-pairs/
Author: Youngsoo Lee
Time complexity: O(n)
"""
from typing import List
import sys
sys.path.insert(0, '..') # hack for importing utils
from utils import ListNode, array2listnode, listnode2array


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        empty_head = pointer = ListNode()
        empty_head.next = head

        while pointer.next and pointer.next.next:
            first = pointer.next
            second = pointer.next.next

            pointer.next = second
            first.next = second.next
            second.next = first
            pointer = first

        return empty_head.next


if __name__ == '__main__':
    s = Solution()

    def runAlgorithm(lists: List[int]):
        return listnode2array(s.swapPairs(array2listnode(lists)))

    assert runAlgorithm([1,2,3,4]) == [2,1,4,3]
    assert runAlgorithm([]) == []
    assert runAlgorithm([1]) == [1]
