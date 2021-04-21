"""
Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Author: Youngsoo Lee
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                nums[ret] = nums[i]
                ret += 1

        return ret


if __name__ == '__main__':
    s = Solution()

    nums = [1,1,2]
    assert s.removeDuplicates(nums) == 2
    assert nums[:2] == [1,2]

    nums = [0,0,1,1,1,2,2,3,3,4]
    assert s.removeDuplicates(nums) == 5
    assert nums[:5] == [0,1,2,3,4]
