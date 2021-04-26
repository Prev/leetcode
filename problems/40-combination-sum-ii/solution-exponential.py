"""
Problem: https://leetcode.com/problems/combination-sum-ii/
Author: Youngsoo Lee
Time complexity: O(2^n)
"""
from typing import List, Dict


class Solution:
    def _run(self, count_dict: Dict[int, int], target: int) -> List[List[int]]:
        if target == 0:
            return [tuple()]

        ret = set()
        for num, count in count_dict.items():
            if target - num < 0 or count <= 0:
                continue

            count_dict[num] -= 1
            result = self._run(count_dict, target - num)
            count_dict[num] += 1

            for tup in result:
                ret.add(tuple(sorted(tup + (num, ))))
        return ret

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        count_dict = {}
        for value in candidates:
            count_dict[value] = count_dict.get(value, 0) + 1

        ret = [list(tup) for tup in self._run(count_dict, target)]
        return ret


if __name__ == '__main__':
    s = Solution()

    assert sorted(s.combinationSum2([10,1,2,7,6,1,5], 8)) == sorted([[1,1,6],[1,2,5],[1,7],[2,6]])
    assert sorted(s.combinationSum2([2,5,2,1,2], 5)) == sorted([[1,2,2],[5]])
