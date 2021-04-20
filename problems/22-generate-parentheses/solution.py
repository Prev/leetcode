"""
Problem: https://leetcode.com/problems/generate-parentheses/
Author: Youngsoo Lee
Time complexity: Hard to calculate
"""
from typing import List


class Solution:
    memoize = {}

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        if n in self.memoize:
            return self.memoize[n]

        candidate = set()

        # Parenthesize `n-1`-length substrings
        for s1 in self.generateParenthesis(n-1):
            candidate.add('(' + s1 + ')')

        # Concatenate two substrings, where the sum of the lengths
        # of the two substrings is `n`.
        for i in range(1, n):
            left = self.generateParenthesis(i)
            right = self.generateParenthesis(n-i)

            for s1 in left:
                for s2 in right:
                    candidate.add(s1 + s2)

        # Record the result since the method is a pure function.
        self.memoize[n] = list(candidate)
        return self.memoize[n]


if __name__ == '__main__':
    s = Solution()

    assert set(s.generateParenthesis(3)) == set(['((()))','(()())','(())()','()(())','()()()'])
    assert s.generateParenthesis(1) == ['()']
    assert len(s.generateParenthesis(4)) == 14
