"""
Problem: https://leetcode.com/problems/permutations/
Author: Youngsoo Lee
Time complexity: O(n^2)
Spcae complexity: O(1)
"""
from typing import List


class Solution:
    def _dfs(self, matrix: List[List[int]], i: int, j: int,
             init_i:int, init_j: int):
        n = len(matrix)
        ni, nj = j, (n - i - 1)

        if (ni, nj) == (init_i, init_j):
            return matrix[i][j]

        ret = self._dfs(matrix, ni, nj, init_i, init_j)
        matrix[ni][nj] = matrix[i][j]

        if (i, j) == (init_i, init_j):
            matrix[i][j] = ret
        return ret

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range((n + 1) // 2):
            for j in range(n - 2 * i - 1):
                print(i, i+j)
                self._dfs(matrix, i, i+j, i, i+j)


if __name__ == '__main__':
    s = Solution()

    def test_solution(matrix, expected):
        s.rotate(matrix)
        assert matrix == expected

    test_solution([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]])
    test_solution([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
                  [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])

    test_solution([[1]], [[1]])
    test_solution([[1,2],[3,4]], [[3,1],[4,2]])
