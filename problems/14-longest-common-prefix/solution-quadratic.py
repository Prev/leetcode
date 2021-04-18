"""
Problem: https://leetcode.com/problems/longest-common-prefix/
Author: Youngsoo Lee
Time complexity: O(n^2) where n is length of `str` and length of `str[i]`
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        n = min([len(s) for s in strs])
        for k in range(n):
            for i in range(1, len(strs)):
                if strs[0][k] != strs[i][k]:
                    return strs[0][0:k]
        return strs[0][:n]


if __name__ == '__main__':
    s = Solution()

    assert s.longestCommonPrefix(['flower','flow','flight']) == 'fl'
    assert s.longestCommonPrefix(['dog','racecar','car']) == ''
    assert s.longestCommonPrefix(['aa','aaa','aaab']) == 'aa'
