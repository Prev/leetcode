"""
Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Author: Youngsoo Lee
Time complexity: O(n^2)
"""

class Solution:
    def _maxTrailingSubstring(self, s: str) -> str:
        wordMap = {}
        n = 0

        for word in s:
            if word in wordMap:
                break
            wordMap[word] = True
            n += 1

        return n

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ret = 0

        for start in range(n):
            substr = s[start:]
            candidate = self._maxTrailingSubstring(substr)
            ret = max(ret, candidate)
        return ret


if __name__ == '__main__':
    s = Solution()

    # The answer is "abc", with the length of 3.
    assert s.lengthOfLongestSubstring('abcabcbb') == 3

    # The answer is "b", with the length of 1.
    assert s.lengthOfLongestSubstring('bbbbb') == 1

    # The answer is "wke", with the length of 3.
    assert s.lengthOfLongestSubstring('pwwkew') == 3

    # The answer is "afbdgcb", with the length of 7.
    assert s.lengthOfLongestSubstring('abcdeafbdgcbb') == 7
