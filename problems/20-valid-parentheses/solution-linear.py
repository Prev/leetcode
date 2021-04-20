"""
Problem: https://leetcode.com/problems/valid-parentheses/
Author: Youngsoo Lee
Time complexity: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        matches = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
            else:
                if len(stack) == 0 or stack.pop() != matches[char]:
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()

    assert s.isValid('()') == True
    assert s.isValid('()[]{}') == True
    assert s.isValid('(]') == False
    assert s.isValid('([)]') == False
    assert s.isValid('{[]}') == True
