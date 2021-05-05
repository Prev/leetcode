"""
Problem: https://leetcode.com/problems/permutations-ii/
Author: Youngsoo Lee
Time complexity: O(n!)
"""
from typing import List


class Solution:
    def _dfs(self, table):
        if sum(table.values()) == 0:
            return [[]]

        ret = []
        for num, count in table.items():
            if count <= 0:
                continue

            table[num] -= 1
            tmp = self._dfs(table)
            table[num] += 1

            for nums2 in tmp:
                ret.append([num] + nums2)

        return ret

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        table = {}
        for num in nums:
            table[num] = table.get(num, 0) + 1
        return self._dfs(table)


if __name__ == '__main__':
    s = Solution()

    assert sorted(s.permuteUnique([1,1,2])) == sorted([[1,1,2],[1,2,1],[2,1,1]])
    assert sorted(s.permuteUnique([1,2,3])) == sorted([
        [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]
    ])

    assert sorted(s.permuteUnique([0,1])) == sorted([[0,1],[1,0]])
    assert sorted(s.permuteUnique([1])) == [[1]]
