"""
Problem: https://leetcode.com/problems/next-permutation/
Author: Youngsoo Lee
Time complexity: O(nlogn)
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            nums[:] = sorted(nums)
            return

        # Sort the remaining part
        nums[i:] = sorted(nums[i:])

        for j in range(i, len(nums)):
            if nums[j] > nums[i-1]:
                # swap
                nums[j], nums[i-1] = nums[i-1], nums[j]
                break


if __name__ == '__main__':
    s = Solution()

    def test_algorithm(nums, expected):
        s.nextPermutation(nums)
        assert nums == expected

    test_algorithm([1,2,3], [1,3,2])
    test_algorithm([3,2,1], [1,2,3])
    test_algorithm([1,1,5], [1,5,1])
    test_algorithm([1], [1])

    test_algorithm([2,3,1], [3,1,2])
    test_algorithm([1,3,2], [2,1,3])
    test_algorithm([5,1,1], [1,1,5])
