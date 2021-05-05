"""
Problem: https://leetcode.com/problems/jump-game-ii/
Author: Youngsoo Lee
Time complexity: O(n^2)
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_count = 0
        i = 0
        while i < len(nums) - 1:
            max_val, max_val_index = 0, i+1
            for j in range(1, nums[i]+1):
                if i + j >= len(nums) - 1:
                    # Can approach to the end after one jump
                    max_val_index = len(nums)
                    break

                if j + nums[i+j] > max_val:
                    max_val = j + nums[i+j]
                    max_val_index = i + j

            i = max_val_index
            jump_count += 1
        return jump_count


if __name__ == '__main__':
    s = Solution()

    assert s.jump([2,3,1,1,4]) == 2
    assert s.jump([2,3,0,1,4]) == 2

    assert s.jump([1,1,1,1]) == 3
    assert s.jump([4,1,1]) == 1
    assert s.jump([2,2,1]) == 1
    assert s.jump([3,2,1]) == 1
    assert s.jump([0]) == 0
