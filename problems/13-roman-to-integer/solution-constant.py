"""
Problem: https://leetcode.com/problems/roman-to-integer/
Author: Youngsoo Lee
Time complexity: O(1)
"""
from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        special_symbols = {'IV': 4, 'IX': 9, 'XL': 40,
                           'XC': 90, 'CD': 400, 'CM': 900}
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000}

        ret = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in special_symbols:
                ret += special_symbols[s[i:i+2]]
                i += 2
                continue

            elif s[i] in symbols:
                ret += symbols[s[i]]
            i += 1
        return ret


if __name__ == '__main__':
    s = Solution()

    assert s.romanToInt('III') == 3
    assert s.romanToInt('IV') == 4
    assert s.romanToInt('IX') == 9
    assert s.romanToInt('LVIII') == 58
    assert s.romanToInt('MCMXCIV') == 1994
