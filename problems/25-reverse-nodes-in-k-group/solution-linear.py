"""
Problem: https://leetcode.com/problems/swap-nodes-in-pairs/
Author: Youngsoo Lee
Time complexity: O(n)
Space complexity: O(k/2)
"""
from typing import List
import sys
sys.path.insert(0, '..') # hack for importing utils
from utils import ListNode, array2listnode, listnode2array


class Solution:
    def _swap_children(self, x0: ListNode, y0: ListNode):
        """ Swap `x0.next` and `y0.next`"""
        x1, y1 = x0.next, y0.next

        if y0 == x1:
            x0.next = y1
            x1.next = y1.next
            y1.next = x1
        else:
            x0.next = y1
            y0.next = x1
            x1.next, y1.next = y1.next, x1.next

        return x1

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        empty_head = pointer = ListNode()
        empty_head.next = head

        # Using stack to perform swapping.
        # For example, if an array [1,2,3,4,5] is given with k=5,
        # we first push to the stack until the pointer approaches to the
        # center (stack=[1,2]). Then, we pop the stack and swap with a next pointer
        # (swap 2 and 4, swap 1 and 5). Note than the center element 3 is ignored.
        # And as swapping changes the order of the linked list, we should update
        # pointer after swapping is performed.
        i = 0
        stack = []

        while pointer.next:
            if i < (k + 1) / 2 - 1:
                # Less than half
                stack.append(pointer)
            elif i == (k + 1) / 2 - 1:
                # Exactly same to the half (in a odd number of k)
                pass
            else:
                # Exceed the half.
                # Check whether the number of following nodes >= k.
                end = pointer
                while i < k and end:
                    i += 1
                    end = end.next
                if end is None:
                    # Not enough remaining nodes. Do not perform swapping.
                    break
                # Swap
                while len(stack):
                    pointer = self._swap_children(stack.pop(), pointer)
                i = 0
                continue

            pointer = pointer.next
            i = (i + 1) % k

        return empty_head.next


if __name__ == '__main__':
    s = Solution()

    def runAlgorithm(lists: List[int], k: int):
        return listnode2array(s.reverseKGroup(array2listnode(lists), k))

    assert runAlgorithm([1,2,3,4,5], 2) == [2,1,4,3,5]
    assert runAlgorithm([1,2,3,4,5], 3) == [3,2,1,4,5]
    assert runAlgorithm([1,2,3,4,5], 1) == [1,2,3,4,5]
    assert runAlgorithm([1], 1) == [1]

    assert runAlgorithm([1,2,3,4,5], 4) == [4,3,2,1,5]
    assert runAlgorithm([1,2,3,4,5], 5) == [5,4,3,2,1]
    assert runAlgorithm([1,2,3,4,5,6,7], 4) == [4,3,2,1,5,6,7]
