"""
Problem: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
Author: Youngsoo Lee
Time complexity: O(NMlogM) where N is length of `s` and
                 M is the length of `words`.
"""
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        m = len(words)
        k = len(words[0]) # length of the words are all same

        # Covert `words` to a dictionary for fast search
        # e.g., {'foo': 0, 'bar': 1, 'the': 2}
        word_index = dict(zip(words, range(n)))

        # `word_ids` contains the word index if s[i:i+k] equals to
        # the any word, -1 otherwise.
        word_ids = [-1] * (n - k + 1)
        for i in range(0, n - k + 1):
            word_ids[i] = word_index.get(s[i:i+k], -1)

        expected = sorted([word_index[word] for word in words])
        ret = []
        for i in range(len(word_ids)):
            idx = [-1] * m
            # Check next `m` words.
            for j in range(m):
                if i + j * k < len(word_ids):
                    idx[j] = word_ids[i + j * k]
            # If next `m` words are equal to the answer in any order,
            # add to the return value.
            if expected == sorted(idx):
                ret.append(i)
        return ret


if __name__ == '__main__':
    s = Solution()

    assert s.findSubstring('barfoothefoobarman', ['foo','bar']) == [0, 9]
    assert s.findSubstring('wordgoodgoodgoodbestword', ['word','good','best','word']) == []
    assert s.findSubstring('barfoofoobarthefoobarman', ['bar','foo','the']) == [6,9,12]

    assert s.findSubstring('wordgoodgoodgoodbestword', ['word','good','best','good']) == [8]
    assert s.findSubstring('aaaaaaaaaaaaaa', ['aa','aa']) == [0,1,2,3,4,5,6,7,8,9,10]
