"""
Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Author: Youngsoo Lee
Time complexity: O(2n) = O(n)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window
        left, right, ret = 0, 0, 0

        occurrences = {}
        while right < len(s):
            occurrences[s[right]] = occurrences.get(s[right], 0) + 1

            while occurrences[s[right]] > 1:
                occurrences[s[left]] -= 1
                left += 1
            
            ret = max(ret, right - left + 1)
            right += 1

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
