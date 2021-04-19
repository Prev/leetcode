"""
Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Author: Youngsoo Lee
Time complexity: O(1) as constraints are restricted
"""
from typing import List


class Solution:
    def _recursive(self, letters: List[List[str]], s: str):
        if len(letters) == 1:
            return [s + letter for letter in letters[0]]

        ret = []
        for letter in letters[0]:
            ret += self._recursive(letters[1:], s + letter)
        return ret

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        rules = ['', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        letters = []
        for digit in digits:
            digit = int(digit)
            if digit > 1:
                letters.append([char for char in rules[digit-1]])

        ret = self._recursive(letters, '')
        return ret


if __name__ == '__main__':
    s = Solution()

    assert s.letterCombinations('23') == ['ad','ae','af','bd','be','bf','cd','ce','cf']
    assert s.letterCombinations('') == []
    assert s.letterCombinations('2') == ['a','b','c']
    assert s.letterCombinations('7') == ['p','q','r','s']
