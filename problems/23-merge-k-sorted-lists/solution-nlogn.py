"""
Problem: https://leetcode.com/problems/merge-k-sorted-lists/
Author: Youngsoo Lee
Time complexity: O(nlogn)) or O(klogN)
                 where N is total number of nodes and k is length of the lists.
"""
from typing import List
import sys
sys.path.insert(0, '..') # hack for importing utils
from utils import ListNode, array2listnode, listnode2array

from heapq import heappush, heappop


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        empty_head = tail = ListNode()

        # Using an incremental number to avoid the duplicated order key.
        # (ListNode object is not comparable)
        i = 0

        heap = []
        for node in lists:
            if node:
                heappush(heap, (node.val, i, node))
                i += 1

        while len(heap):
            _, _, node = heappop(heap)

            tail.next = node
            tail = tail.next

            if node.next:
                heappush(heap, (node.next.val, i, node.next))
                i += 1

        return empty_head.next


if __name__ == '__main__':
    s = Solution()

    def runAlgorithm(lists: List[List[int]]):
        return listnode2array(s.mergeKLists([array2listnode(l) for l in lists]))

    assert runAlgorithm([[1,4,5],[1,3,4],[2,6]]) == [1,1,2,3,4,4,5,6]
    assert runAlgorithm([]) == []
    assert runAlgorithm([[]]) == []
