"""
Problem: https://leetcode.com/problems/first-missing-positive/
Author: Youngsoo Lee
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List

# This is a tricky solution.
# We modifiy the `nums` itself to record the found positive numbers.
# This is an example of the case of nums = [4,-1,1,2].
# First, we have to mark nums[3] to represent that the number four exists.
# But before marking, we have to process the element in `nums[3]`, `2`.
# We do it in a recursive way.


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        special_num = n + 999

        def _recursive(i: int):
            val = nums[i]

            # We only need to consider the numbers in the range [0, n].
            if 0 < val <= n and nums[val - 1] != special_num:
                # Mark the current number to avoid duplicated recursion.
                nums[i] = -1
                if i != val - 1:
                    # Recursively process before marking the `nums[val-1]` to a special number.
                    _recursive(val - 1)
                # Replace to the special number to let know that this number exists.
                nums[val-1] = special_num

        for i in range(n):
            _recursive(i)

        for i in range(n):
            if nums[i] != special_num:
                return i + 1
        return n + 1


if __name__ == '__main__':
    s = Solution()

    assert s.firstMissingPositive([1,2,0]) == 3
    assert s.firstMissingPositive([3,4,-1,1]) == 2
    assert s.firstMissingPositive([7,8,9,11,12]) == 1
