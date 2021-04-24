"""
Problem: https://leetcode.com/problems/sudoku-solver/
Author: Youngsoo Lee
Time complexity: O(n^m) where n is the number of possibilities for each square
                 (i.e., 9 in classic Sudoku) and m is the number of spaces that are blank.
"""
from typing import List


class Solution:
    def _is_possible(self, row: int, col: int, value: int):
        value = str(value)
        for k in range(9):
            if value == self.board[row][k]:
                return False
            if value == self.board[k][col]:
                return False
            # Sub-box elements
            if value == self.board[3 * (row // 3) + (k // 3)][3 * (col // 3) + (k % 3)]:
                return False
        return True

    def _visit(self, i: int):
        if i == 81:
            return True

        row = i // 9
        col = i % 9

        if self.board[row][col] != '.':
            return self._visit(i+1)

        for num in range(1, 10):
            if self._is_possible(row, col, num):
                self.board[row][col] = str(num)
                if self._visit(i+1) == True:
                    return True
                self.board[row][col] = '.'

        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self._visit(0)


if __name__ == '__main__':
    s = Solution()

    board = [['5','3','.','.','7','.','.','.','.'],
            ['6','.','.','1','9','5','.','.','.'],
            ['.','9','8','.','.','.','.','6','.'],
            ['8','.','.','.','6','.','.','.','3'],
            ['4','.','.','8','.','3','.','.','1'],
            ['7','.','.','.','2','.','.','.','6'],
            ['.','6','.','.','.','.','2','8','.'],
            ['.','.','.','4','1','9','.','.','5'],
            ['.','.','.','.','8','.','.','7','9']]

    s.solveSudoku(board)

    assert board == [['5','3','4','6','7','8','9','1','2'],
                    ['6','7','2','1','9','5','3','4','8'],
                    ['1','9','8','3','4','2','5','6','7'],
                    ['8','5','9','7','6','1','4','2','3'],
                    ['4','2','6','8','5','3','7','9','1'],
                    ['7','1','3','9','2','4','8','5','6'],
                    ['9','6','1','5','3','7','2','8','4'],
                    ['2','8','7','4','1','9','6','3','5'],
                    ['3','4','5','2','8','6','1','7','9']]
