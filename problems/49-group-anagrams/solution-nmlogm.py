"""
Problem: https://leetcode.com/problems/group-anagrams/
Author: Youngsoo Lee
Time complexity: O(nmlogm) where n is the length of `strs`,
                 and m is maximum length of a string in `strs`.
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i, s in enumerate(strs):
            sorted_s = ''.join(sorted(s))

            if sorted_s not in ans:
                ans[sorted_s] = []
            ans[sorted_s].append(s)

        return list(ans.values())


if __name__ == '__main__':
    s = Solution()

    output = s.groupAnagrams(['eat','tea','tan','ate','nat','bat'])
    expected = [['bat'],['nat','tan'],['ate','eat','tea']]
    for i in range(len(output)):
        output[i] = sorted(output[i])
        expected[i] = sorted(expected[i])
    assert sorted(output) == sorted(expected)

    assert s.groupAnagrams(['']) == [['']]
    assert s.groupAnagrams(['a']) == [['a']]
