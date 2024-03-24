"""
https://leetcode.com/problems/top-k-frequent-elements/description/
----
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
"""

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1

        snums = len(nums)
        frequencys = [[] for _ in range(snums+1)]

        for num in mapping:
            frequencys[mapping[num]].append(num)

        i = snums
        ks = []
        while i > 0:

            frequency = frequencys[i]
            for n in frequency:
                ks.append(n)
            i -= 1
            if len(ks) == k:
                return ks
        return [] 
