"""
Problem: https://leetcode.com/problems/powx-n/
Author: Youngsoo Lee
Time complexity: O(1)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n


if __name__ == '__main__':
    s = Solution()

    assert s.myPow(2.00000, 10) == 1024.00000
    assert round(s.myPow(2.10000, 3), 4) == 9.26100
    assert s.myPow(2.00000, -2) == 0.25000
