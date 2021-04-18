"""
Problem: https://leetcode.com/problems/3sum/
Author: Youngsoo Lee
Time complexity: O(n^2)
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # The only case that the triplet contains all equal elements
        if count.get(0, 0) >= 3:
            ret.add((0, 0, 0))

        distinct_nums = list(count.keys())
        for i in range(len(distinct_nums)):
            for j in range(i+1, len(distinct_nums)):
                a, b = distinct_nums[i], distinct_nums[j]
                c = -(a + b)
                if c not in count:
                    continue

                # Two cases available.
                # 1) All different elements: (a, b, c)
                # 2) Two elements of the triplet are the same: (a, a, b)
                if c not in (a, b) or count[c] >= 2:
                    triplet = tuple(sorted((a, b, c)))
                    ret.add(triplet)

        return list(ret)


if __name__ == '__main__':
    s = Solution()

    assert s.threeSum([-1,0,1,2,-1,-4]) in ([(-1,-1,2),(-1,0,1)], [(-1,0,1), (-1,-1,2)])
    assert s.threeSum([]) == []
    assert s.threeSum([0]) == []
    assert s.threeSum([0, 0, 0, 0, 0]) == [(0, 0, 0)]
