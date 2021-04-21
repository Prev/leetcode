"""
Problem: https://leetcode.com/problems/divide-two-integers/
Author: Youngsoo Lee
Time complexity: O(1)
"""
from typing import List

import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = dividend / divisor

        if a > 0 :
            return max(min(math.floor(a), 2 ** 31 - 1), -2 ** 31)
        else:
            return max(min(-math.floor(-a), 2 ** 31 - 1), -2 ** 31)


if __name__ == '__main__':
    s = Solution()

    assert s.divide(10, 3) == 3
    assert s.divide(7, -3) == -2
    assert s.divide(0, 1) == 0
    assert s.divide(1, 1) == 1
