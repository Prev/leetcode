"""
Problem: https://leetcode.com/problems/integer-to-roman/
Author: Youngsoo Lee
Time complexity: O(1)
"""
from typing import List


class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = [('I', 'V'), ('X', 'L'), ('C', 'D'), ('M', )]
        ret = ''

        while num > 0:
            d = num % 10
            s = symbols[0]

            if d == 0:   pass
            if d <= 3:   ret = (s[0] * d) + ret
            elif d == 4: ret = (s[0] + s[1]) + ret
            elif d == 5: ret = (s[1]) + ret
            elif d == 9: ret = (s[0] + symbols[1][0]) + ret
            else:        ret = (s[1] + s[0] * (d - 5)) + ret

            num = num // 10
            symbols = symbols[1:]

        return ret


if __name__ == '__main__':
    s = Solution()

    assert s.intToRoman(3) == 'III'
    assert s.intToRoman(4) == 'IV'
    assert s.intToRoman(9) == 'IX'
    assert s.intToRoman(58) == 'LVIII'
    assert s.intToRoman(1994) == 'MCMXCIV'
