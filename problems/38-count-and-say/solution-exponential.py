"""
Problem: https://leetcode.com/problems/count-and-say/
Author: Youngsoo Lee
Time complexity: O(2^n)
"""
from typing import List


class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'

        for _ in range(1, n):
            count = 1
            new_s = ''
            for i in range(len(s)):
                if i == len(s) - 1 or s[i+1] != s[i]:
                    new_s += f'{count}{s[i]}'
                    count = 1
                else:
                    count += 1
            s = new_s
        return s


if __name__ == '__main__':
    s = Solution()

    assert s.countAndSay(1) == '1'
    assert s.countAndSay(4) == '1211'
