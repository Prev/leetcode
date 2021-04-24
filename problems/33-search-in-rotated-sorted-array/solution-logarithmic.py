"""
Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/
Author: Youngsoo Lee
Time complexity: O(logn)
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right + 1) // 2

            if nums[mid] == target:
                return mid
            elif nums[left] > nums[right] and nums[mid] <= nums[right]:
                # Rotating point is in the left range
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1 # search right
                else:
                    right = mid - 1 # search left
            elif nums[left] > nums[right] and nums[mid] > nums[right]:
                # Rotating point is in the right range
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()

    assert s.search([7,8,1,2,3,4,5,6], 2) == 3
    assert s.search([3,4,5,6,7,8,1,2], 1) == 6
    assert s.search([3,4,5,6,7,8,1,2], 3) == 0

    assert s.search([3,1], 3) == 0
    assert s.search([2,3,4,5,6,7,8,9,1], 9) == 7
    assert s.search([4,5,6,7,0,1,2], 0) == 4
    assert s.search([4,5,6,7,0,1,2], 3) == -1
    assert s.search([1], 0) == -1
