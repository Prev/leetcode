"""
Problem: https://leetcode.com/problems/string-to-integer-atoi/
Author: Youngsoo Lee
Time complexity: O(n)
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: trim leading whitespace
        s = s.lstrip()

        if s == '':
            return 0

        # Step 2: Check for the symbols '+' and '-'
        sign = 1
        if s[0] == '-':
            s = s[1:]
            sign = -1
        elif s[0] == '+':
            s = s[1:]

        # Step 3: Read until non-digit char found
        digit_chars = [c for c in '0123456789']
        i = 0
        while i < len(s) and s[i] in digit_chars:
            i += 1

        # Step 4: Convert digits into an integer
        if s[:i] == '':
            num = 0
        else:
            num = int(s[:i]) * sign

        # Step 5: Check out of range
        num = max(num, 2 ** 31 * -1)
        num = min(num, 2 ** 31 - 1)
        return num


if __name__ == '__main__':
    s = Solution()

    assert s.myAtoi('42') == 42
    assert s.myAtoi('     42') == 42
    assert s.myAtoi('4193 with words') == 4193
    assert s.myAtoi('words and 987') == 0
    assert s.myAtoi('-91283472332') == -2147483648
