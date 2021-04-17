"""
Problem: https://leetcode.com/problems/longest-palindromic-substring/
Author: Youngsoo Lee
Time complexity: O(n^2)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ret = (0, 0)

        # In this iteration, we assume that length of the palindromic
        # substring is an "odd" number, and set the center char to be `s[i]`.
        for i in range(n):
            pos = (i, i)
            k = min(i, n - i - 1)

            # Search for `i-k ~ i+k` characters
            for j in range(1, k+1):
                # Check whether it is a palindromic substring
                if s[i-j] == s[i+j]:
                    pos = (i-j, i+j)
                else:
                    break

            if pos[1] - pos[0] > ret[1] - ret[0]:
                ret = pos

        # In this iteration, we assume that length of the palindromic
        # substring is an "even" number.
        for i in range(n-1):
            if s[i] != s[i+1]:
                continue

            pos = (i, i+1)
            k = min(i, n - i - 2)

            # Search for `i-k ~ i+k+1` characters
            for j in range(1, k+1):
                if s[i-j] == s[i+j+1]:
                    pos = (i-j, i+j+1)
                else:
                    break

            if pos[1] - pos[0] > ret[1] - ret[0]:
                ret = pos

        start, end = ret
        return s[start:end+1]


if __name__ == '__main__':
    s = Solution()

    assert s.longestPalindrome('babad') in ('aba', 'bab')
    assert s.longestPalindrome('cbbd') == 'bb'
    assert s.longestPalindrome('a') == 'a'
    assert s.longestPalindrome('ac') in ('a', 'c')
