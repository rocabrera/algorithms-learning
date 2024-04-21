"""
https://leetcode.com/problems/sqrtx/
----
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""

class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0: return 0
        if x == 1: return 1
        
        l, r = 0, (x // 2)

        while l <= r:
            mid = (l + r) // 2
            target = mid*mid

            if target == x:
                return mid
            elif target > x:
                r = mid - 1
            else:
                l = mid + 1

        return r