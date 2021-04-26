"""
Problem: https://leetcode.com/problems/first-missing-positive/
Author: Youngsoo Lee
Time complexity: O(nlogn)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        to_find = 1
        for val in nums:
            if val > to_find:
                return to_find
            elif val == to_find:
                to_find += 1

        return to_find


if __name__ == '__main__':
    s = Solution()

    assert s.firstMissingPositive([1,2,0]) == 3
    assert s.firstMissingPositive([3,4,-1,1]) == 2
    assert s.firstMissingPositive([7,8,9,11,12]) == 1
