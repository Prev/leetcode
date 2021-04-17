"""
Problem: https://leetcode.com/problems/reverse-integer/
Author: Youngsoo Lee
Time complexity: O(1)
"""

from typing import Tuple, List


class Solution:
    def _split_digit(self, x: int, reverse=False) -> List[int]:
        x = abs(x)
        arr = []

        # Length of the maximum integer is 10.
        for n in range(0, 10):
            arr.append(x // (10 ** (9-n)) % 10)

        if reverse:
            while arr[0] == 0:
                arr = arr[1:]
            arr = [0] * (10 - len(arr)) + list(reversed(arr))
        return arr

    def _is_overflowed(self, arr: List[int], to_compare: List[int]) -> bool:
        for i in range(0, 10):
            if arr[i] > to_compare[i]:
                return True
            elif arr[i] < to_compare[i]:
                return False
        return True

    def reverse(self, x: int) -> int:
        if x == 0:
            return x

        arr = self._split_digit(x, reverse=True)
        if x < 0 and self._is_overflowed(arr, self._split_digit(2 ** 31 * -1)):
            # Negative overflow
            return 0
        elif x > 0 and self._is_overflowed(arr, self._split_digit(2 ** 31 -1)):
            # Positive overflow
            return 0

        ret = 0
        for i, val in enumerate(arr):
            ret += val * (10 ** (len(arr) - i - 1))

        return ret * (-1 if x < 0 else 1)


if __name__ == '__main__':
    s = Solution()

    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(0) == 0
    assert s.reverse(901000) == 109

    # Out of range
    assert s.reverse(2 ** 31 * -1) == 0
    assert s.reverse(1534236469) == 0
    assert s.reverse(-1534236469) == 0
