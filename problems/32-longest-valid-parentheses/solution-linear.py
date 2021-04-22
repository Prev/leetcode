"""
Problem: https://leetcode.com/problems/longest-valid-parentheses/
Author: Youngsoo Lee
Time complexity: O(n)
"""
from typing import List


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ret = 0
        stack = [] # Stores the indexes of the left parenthesis.
        invalid_index = -1

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif len(stack) == 0:
                stack = []
                invalid_index = i
            else:
                stack.pop()

                if len(stack) == 0:
                    ret = max(ret, i - invalid_index)
                else:
                    ret = max(ret, i - max(invalid_index, stack[-1]))

        return ret


if __name__ == '__main__':
    s = Solution()

    assert s.longestValidParentheses('(()') == 2
    assert s.longestValidParentheses(')()())') == 4
    assert s.longestValidParentheses('0') == 0

    assert s.longestValidParentheses(')(') == 0
    assert s.longestValidParentheses('()(()') == 2
    assert s.longestValidParentheses('()(()()') == 4
    assert s.longestValidParentheses('()((())') == 4
