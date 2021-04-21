"""
Problem: https://leetcode.com/problems/remove-element/
Author: Youngsoo Lee
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ret = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ret] = nums[i]
                ret += 1
        return ret


if __name__ == '__main__':
    s = Solution()

    nums = [3,2,2,3]
    assert s.removeElement(nums, 3) == 2
    assert nums[:2] == [2,2]

    nums = [0,1,2,2,3,0,4,2]
    assert s.removeElement(nums, 2) == 5
    assert sorted(nums[:5]) == sorted([0,1,4,0,3])
