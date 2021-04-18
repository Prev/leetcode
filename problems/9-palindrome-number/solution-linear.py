"""
Problem: https://leetcode.com/problems/palindrome-number/
Author: Youngsoo Lee
Time complexity: O(n)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    s = Solution()

    assert s.isPalindrome(121) == True
    assert s.isPalindrome(-121) == False
    assert s.isPalindrome(10) == False
    assert s.isPalindrome(-101) == False
