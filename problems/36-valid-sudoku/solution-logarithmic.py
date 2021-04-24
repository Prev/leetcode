"""
Problem: https://leetcode.com/problems/valid-sudoku/
Author: Youngsoo Lee
Time complexity: O(1)
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        subboxes = [{} for _ in range(9)]

        for i in range(0, 9):
            for j in range(0, 9):
                v = board[i][j]
                if v == '.':
                    continue

                subbox_index = 3 * (i // 3) + (j // 3)
                if v in rows[i] or v in cols[j] or v in subboxes[subbox_index]:
                    return False

                rows[i][v] = cols[j][v] = subboxes[subbox_index][v] = True

        return True

if __name__ == '__main__':
    s = Solution()

    assert s.isValidSudoku(
        [['5','3','.','.','7','.','.','.','.']
        ,['6','.','.','1','9','5','.','.','.']
        ,['.','9','8','.','.','.','.','6','.']
        ,['8','.','.','.','6','.','.','.','3']
        ,['4','.','.','8','.','3','.','.','1']
        ,['7','.','.','.','2','.','.','.','6']
        ,['.','6','.','.','.','.','2','8','.']
        ,['.','.','.','4','1','9','.','.','5']
        ,['.','.','.','.','8','.','.','7','9']]) == True

    assert s.isValidSudoku(
        [['8','3','.','.','7','.','.','.','.']
        ,['6','.','.','1','9','5','.','.','.']
        ,['.','9','8','.','.','.','.','6','.']
        ,['8','.','.','.','6','.','.','.','3']
        ,['4','.','.','8','.','3','.','.','1']
        ,['7','.','.','.','2','.','.','.','6']
        ,['.','6','.','.','.','.','2','8','.']
        ,['.','.','.','4','1','9','.','.','5']
        ,['.','.','.','.','8','.','.','7','9']]) == False
