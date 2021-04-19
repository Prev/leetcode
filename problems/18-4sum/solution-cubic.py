"""
Problem: https://leetcode.com/problems/4sum/
Author: Youngsoo Lee
Time complexity: O(n^3)
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = set()

        table = {}
        for i, n in enumerate(nums):
            table[n] = i

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    a, b, c = nums[i], nums[j], nums[k]
                    d = target - (a + b + c)

                    # Index of `d` should be greater than both `a`, `b`, and `c`,
                    # to avoid the duplication of each num.
                    if d in table and table[d] > k:
                        ret.add(tuple(sorted((a, b, c, d))))

        return list(ret)


if __name__ == '__main__':
    s = Solution()

    assert s.fourSum([1,0,-1,0,-2,2], 0) == [(-2,-1,1,2),(-1,0,0,1),(-2,0,0,2)]
    assert s.fourSum([2,2,2,2,2], 8) == [(2,2,2,2)]
