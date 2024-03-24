"""
https://leetcode.com/problems/group-anagrams/description/
----
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mapping = {}
        for word in strs:
            sword = ''.join(sorted(word))

            if sword not in mapping:
                mapping[sword] = [word]
            else:
                mapping[sword].append(word)

        return list(mapping.values())

strs = ["eat","tea","tan","ate","nat","bat"]
result = Solution().groupAnagrams(strs)
print(result)
