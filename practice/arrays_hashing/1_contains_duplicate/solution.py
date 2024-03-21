"""
https://leetcode.com/problems/contains-duplicate/description/
----
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Constraints:

1 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        values = {}

        for num in nums:
            if num not in values:
                values[num] = 1
            else:
                values[num] += 1
                
            if values[num]>=2:
                return True

        return False

# Took from solutions
# class Solution:
#     def containsDuplicate(self, nums):
#         hset = set()
#         for idx in nums:
#             if idx in hset:
#                 return True
#             else:
#                 hset.add(idx)
#
#         return False
