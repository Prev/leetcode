"""
Utility functions for leetcode problems.
"""
from typing import List


class ListNode:
    """ Definition for singly-linked list used in leetcode"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def array2listnode(array: List[int]):
    """ Convert array(list) to linked list of ListNodes
    """
    head = ListNode(array[0])
    tail = head

    for i in range(1, len(array)):
        tail.next = ListNode(array[i])
        tail = tail.next

    return head


def listnode2array(head: ListNode):
    """ Convert linked list of ListNodes to array(list)
    """
    ret = []
    while head:
        ret.append(head.val)
        head = head.next
    return ret
