"""
Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/
Author: Youngsoo Lee
Time complexity: O(m+n)
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index1 = 0
        index2 = 0

        n = len(nums1) + len(nums2)
        nums_merged = [0] * n
        i = 0

        while i < n:
            value1 = nums1[index1] if index1 < len(nums1) else None
            value2 = nums2[index2] if index2 < len(nums2) else None

            if value1 is not None and (value2 is None or value1 < value2):
                nums_merged[i] = value1
                index1 += 1
            else:
                nums_merged[i] = value2
                index2 += 1

            i += 1

        if n % 2 == 0:
            return (nums_merged[n // 2 - 1] + nums_merged[n // 2]) / 2
        else:
            return nums_merged[(n - 1) // 2]


if __name__ == '__main__':
    s = Solution()
    assert s.findMedianSortedArrays([1, 3], [2]) == 2
    assert s.findMedianSortedArrays([], [2, 3]) == 2.5
    assert s.findMedianSortedArrays([], [2]) == 2
    assert s.findMedianSortedArrays([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25]) == 11
    assert s.findMedianSortedArrays([1, 3, 8, 9, 15], [7, 11, 18, 19, 21]) == 10
