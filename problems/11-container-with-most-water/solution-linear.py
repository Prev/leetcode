"""
Problem: https://leetcode.com/problems/container-with-most-water/
Author: Youngsoo Lee
Time complexity: O(n)
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ret = 0

        while l <= r:
            ret = max(ret, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ret


if __name__ == '__main__':
    s = Solution()

    assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert s.maxArea([1,1]) == 1
    assert s.maxArea([4,3,2,1,4]) == 16
    assert s.maxArea([1,2,1]) == 2
