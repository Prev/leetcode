"""
Problem: https://leetcode.com/problems/3sum-closest/
Author: Youngsoo Lee
Time complexity: O(n^2)
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ret = sum(nums[0:3])
        nums = list(sorted(nums))

        for i in range(1, len(nums)-1):
            left, right = i-1, i+1

            while left >= 0 and right < len(nums):
                three_sum = nums[left] + nums[right] + nums[i]
                if three_sum == target:
                    return target

                if abs(three_sum - target) < abs(ret - target):
                    ret = three_sum

                if three_sum < target:
                    right += 1
                else:
                    left -= 1
        return ret


if __name__ == '__main__':
    s = Solution()

    assert s.threeSumClosest([-1,2,1,-4], 1) == 2
