"""
Problem: https://leetcode.com/problems/multiply-strings/
Author: Youngsoo Lee
Time complexity: O(nm) where n is length of num1 and
                 m is length of num2
"""
from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        arr = [0] * (max(n1, n2) * 2)

        for i in range(n2):
            for j in range(n1):
                mul = int(num2[n2 - i - 1]) * int(num1[n1 - j - 1])
                carry, sum_ = (mul // 10), (mul % 10)

                exponent = i + j
                arr[exponent] += sum_
                arr[exponent + 1] += carry

        for i in range(len(arr)):
            while arr[i] >= 10:
                arr[i] -= 10
                arr[i+1] += 1

        ret = ''
        leading_zero = True
        for i in reversed(range(len(arr))):
            if leading_zero and arr[i] == 0:
                continue
            leading_zero = False
            ret += str(arr[i])

        if ret == '':
            return '0'

        return ret


if __name__ == '__main__':
    s = Solution()

    assert s.multiply('2', '3') == '6'
    assert s.multiply('123', '456') == '56088'

    assert s.multiply('999', '999') == '998001'
    assert s.multiply('123456789', '987654321') == '121932631112635269'
