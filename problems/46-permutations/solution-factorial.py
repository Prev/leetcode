"""
Problem: https://leetcode.com/problems/permutations/
Author: Youngsoo Lee
Time complexity: O(n!)
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        ret = []
        for i in range(len(nums)):
            for nums2 in self.permute(nums[:i] + nums[i+1:]):
                ret.append([nums[i]] + nums2)
        return ret


if __name__ == '__main__':
    s = Solution()

    assert sorted(s.permute([1,2,3])) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
    assert sorted(s.permute([0,1])) == sorted([[0,1],[1,0]])
    assert sorted(s.permute([1])) == [[1]]
