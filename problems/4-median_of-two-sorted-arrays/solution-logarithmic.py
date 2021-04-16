"""
Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/
Author: Youngsoo Lee
Time complexity: O(log(min(m,n)))
Video referenced: https://www.youtube.com/watch?v=LPFhl65R7ww
"""

from typing import List, Tuple


class Solution:
    def _getSafeValues(self, list1: List[int], list2: List[int],
                      index1: int, index2: int) -> Tuple[float, float]:
        if index1 < 0 or index1 >= len(list1):
            return (list2[index2], )
        elif index2 < 0 or index2 >= len(list2):
            return (list1[index1], )
        else:
            return list1[index1], list2[index2]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        if m > n:
            # Force `nums1` to be a list with a smaller length
            nums1, nums2, m, n = nums2, nums1, n, m

        if m == 0:
            if n % 2 == 1:
                return nums2[n // 2]
            else:
                return (nums2[n // 2 - 1] + nums2[n // 2]) / 2

        istart = 0
        iend = m

        while istart <= iend:
            i = (istart + iend) // 2
            # As partition always equally divide the list,
            # we can derive that `i + j = (m + n + 1) / 2`.
            j = (m + n + 1) // 2 - i

            if i < m and nums1[i] < nums2[j-1]:
                # Move the partition to the right
                istart = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # Move the partition to the left
                iend = i - 1
            else:
                max_of_left = max(self._getSafeValues(nums1, nums2, i-1, j-1))
                min_of_right = min(self._getSafeValues(nums1, nums2, i, j))

                if (m + n) % 2 == 1:
                    return max_of_left
                else:
                    return (max_of_left + min_of_right) / 2


if __name__ == '__main__':
    s = Solution()
    assert s.findMedianSortedArrays([1, 3], [2]) == 2
    assert s.findMedianSortedArrays([], [2, 3]) == 2.5
    assert s.findMedianSortedArrays([], [2]) == 2
    assert s.findMedianSortedArrays([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25]) == 11
    assert s.findMedianSortedArrays([1, 3, 8, 9, 15], [7, 11, 18, 19, 21]) == 10
