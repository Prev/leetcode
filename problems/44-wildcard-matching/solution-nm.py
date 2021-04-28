"""
Problem: https://leetcode.com/problems/wildcard-matching/
Author: Youngsoo Lee
Time complexity: O(nm) where n is length of `s` and
                 m is length of `p`.
"""
from typing import List


class Solution:
    def _search(self, s: str, p: str) -> bool:
        """ Search string with pattern without wildcard feature """
        m = len(p)
        if m == 0:
            return 0

        for i in range(len(s) - m + 1):
            is_matched = True
            for j in range(len(p)):
                if p[j] not in (s[i+j], '?'):
                    is_matched = False
                    break
            if is_matched:
                return i
        return -1

    def isMatch(self, s: str, p: str) -> bool:
        if '*' not in p:
            return len(s) == len(p) and self._search(s, p) == 0

        while '**' in p:
            p = p.replace('**', '*')
        subpatterns = p.split('*')

        for k in range(len(subpatterns)):
            subp = subpatterns[k]
            m = len(subp)
            index = self._search(s, subp)

            if index == -1:
                return False

            if k == 0 and index != 0:
                # The first pattern should be occured in the front of the string.
                # (Note that the leading wildcard also returns 0.)
                return False

            if k == len(subpatterns) - 1:
                # The last pattern should match to the end of the string.
                return self._search(s[len(s)-m:], subp) == 0

            s = s[index+m:]


if __name__ == '__main__':
    s = Solution()

    assert s.isMatch('aa', 'a') == False
    assert s.isMatch('aa', '*') == True
    assert s.isMatch('cb', '?a') == False
    assert s.isMatch('adceb', '*a*b') == True
    assert s.isMatch('acdcb', 'a*c?b') == False

    assert s.isMatch('aaaaaab', 'a*a*a*b') == True
    assert s.isMatch('acbcdabeadbad', '*a*b?d') == True
    assert s.isMatch('aa', '??') == True
    assert s.isMatch('acdqwcbqwec', '*b*') == True
    assert s.isMatch('aaaaaaaaaababaaa', '**********') == True
