"""
Problem: https://leetcode.com/problems/implement-strstr/
Author: Youngsoo Lee
Time complexity: O(n^2)
"""
from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i

        return -1


if __name__ == '__main__':
    s = Solution()

    assert s.strStr('hello', 'll') == 2
    assert s.strStr('aaaaa', 'bba') == -1
    assert s.strStr('', '') == 0
