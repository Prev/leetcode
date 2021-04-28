"""
Problem: https://leetcode.com/problems/trapping-rain-water/
Author: Youngsoo Lee
Time complexity: O(n)
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ret = 0
        n = len(height)

        # `lmax[i]`: maximum value of left elements of the i-th node.
        # `rmax[i]`: maximum value of right elements of the i-th node.
        lmax, rmax = [0] * n, [0] * n
        for i in range(1, n):
            lmax[i] = max(lmax[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            rmax[i] = max(rmax[i+1], height[i+1])

        for i in range(n):
            if height[i] <= lmax[i] and height[i] <= rmax[i]:
                # Higher bars exist in both left and right sides.
                ret += min(lmax[i], rmax[i]) - height[i]
        return ret


if __name__ == '__main__':
    s = Solution()

    assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert s.trap([4,2,0,3,2,5]) == 9
