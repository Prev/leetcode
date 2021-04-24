"""
Problem: https://leetcode.com/problems/combination-sum/
Author: Youngsoo Lee
Time complexity: O(nm) where n is the length of `candidates`
                 and m is the maximum value of `target`.
"""
from typing import List


class Solution:
    memoize = {}

    def _run(self, candidates: List[int], target: int) -> List[List[int]]:
        if target in self.memoize:
            return self.memoize[target]
        if target == 0:
            return [tuple()]

        ret = set()
        for v in candidates:
            if target - v < 0:
                continue
            for cands0 in self._run(candidates, target - v):
                ret.add(tuple(sorted(cands0 + (v, ))))

        self.memoize[target] = ret
        return ret

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.memoize = {}
        return [list(tup) for tup in self._run(candidates, target)]


if __name__ == '__main__':
    s = Solution()

    assert s.combinationSum([2,3,6,7], 7) == [[2,2,3],[7]]
    assert s.combinationSum([2,3,5], 8) == [[2,2,2,2],[2,3,3],[3,5]]
    assert s.combinationSum([2], 1) == []
    assert s.combinationSum([1], 1) == [[1]]
    assert s.combinationSum([1], 2) == [[1,1]]
