"""
Problem: https://leetcode.com/problems/zigzag-conversion/
Author: Youngsoo Lee
Time complexity: O(n)
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1:
            return s

        ret = ''
        # Iterate from the first row to the last row of the zigzag pattern.
        for rowid in range(numRows):
            # The spaces between chracters follow a specific pattern.
            # For example, if numRows=4, the spaces of each row whould be (6, ), (4, 2), (2, 4), and (6, ).
            if rowid == 0 or rowid == numRows - 1:
                spaces_repeated = ((numRows - 1) * 2, (numRows - 1) * 2)
            else:
                spaces_repeated = ((numRows - 1 - rowid) * 2, 2 * rowid)

            index = rowid
            flip = 0

            # Visit to the end of each row
            while index < len(s):
                ret += s[index]
                index += spaces_repeated[flip]
                flip = (flip + 1) % 2

        return ret

if __name__ == '__main__':
    s = Solution()

    assert s.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert s.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert s.convert('A', 1) == 'A'
