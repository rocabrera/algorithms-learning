"""
https://leetcode.com/problems/longest-consecutive-sequence/description/
----
Given an unsorted array of integers nums, return the length of 
the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hsnums = set(nums)

        nlargest = 0
        for num in nums:
            if num-1 in hsnums:
                continue
            elif num in hsnums: 
                ncurrent = 1
                tempnum = num + 1
                while  tempnum in hsnums:
                    tempnum += 1
                    ncurrent += 1
                if nlargest < ncurrent:
                    nlargest = ncurrent

        return nlargest

nums = [0,3,7,2,5,8,4,6,0,1]
result = Solution().longestConsecutive(nums)
print(result)