"""
Problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Author: Youngsoo Lee
Time complexity: O(logn)
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_pos, last_pos = -1, -1

        # Find first pos
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right + 1) // 2

            if target == nums[mid] and (mid == 0 or nums[mid-1] < target):
                first_pos = mid
                break
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        # Find last pos
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right + 1) // 2

            if target == nums[mid] and (mid == len(nums) - 1 or nums[mid+1] > target):
                last_pos = mid
                break
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return [first_pos, last_pos]


if __name__ == '__main__':
    s = Solution()

    assert s.searchRange([5,7,7,8,8,10], 8) == [3,4]
    assert s.searchRange([5,7,7,8,8,10], 6) == [-1,-1]
    assert s.searchRange([], 0) == [-1,-1]

    assert s.searchRange([1,2,2,2,2,3], 2) == [1,4]
    assert s.searchRange([2,2], 2) == [0,1]
