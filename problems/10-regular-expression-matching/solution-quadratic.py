"""
Problem: https://leetcode.com/problems/regular-expression-matching/
Author: Youngsoo Lee
Time complexity: O(n^2) -> Not confident
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True

        if len(p) > 1 and p[1] == '*':
            # Start `i` from `-1` since wildcard(*) matches zero+ elements.
            for i in range(-1, len(s)):
                # Interate until char matches to the preceding element.
                if i == -1 or p[0] in ('.', s[i]):
                    # If any of the sub-call returns true, we can say that
                    # the string is matched to the pattern
                    if self.isMatch(s[i+1:], p[2:]):
                        return True
                else:
                    # Should break the iteration if the char does not match
                    # to the preceding element
                    break
            return False

        elif len(s) > 0 and len(p) > 0 and (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])
        else:
            return False


if __name__ == '__main__':
    s = Solution()

    assert s.isMatch('aa', 'a') == False
    assert s.isMatch('aa', 'a*') == True
    assert s.isMatch('ab', '.*') == True
    assert s.isMatch('aab', 'c*a*b') == True
    assert s.isMatch('mississippi', 'mis*is*p*.') == False

    assert s.isMatch('aa', 'aab') == False
    assert s.isMatch('ab', '.*c') == False
    assert s.isMatch('aaa', 'a*a') == True
    assert s.isMatch('aaa', 'a.*a') == True
    assert s.isMatch('a', 'ab*') == True
