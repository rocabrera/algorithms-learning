"""
https://leetcode.com/problems/3sum/description/
----
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        triplets = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while r > l:
                threeSum = num + nums[l] + nums[r]
                if  threeSum == 0:
                    triplets.append([num, nums[l], nums[r]]) 
                    l += 1
                    while r > l and nums[l] == nums[l-1]:
                        l+=1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
            
        return triplets
