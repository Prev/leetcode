"""
Problem: https://leetcode.com/problems/two-sum/
Author: Youngsoo Lee
Time complexity: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(nums):
            if num in table:
                return [table[num], i]

            table[target - num] = i


if __name__ == '__main__':
    s = Solution()
    
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
