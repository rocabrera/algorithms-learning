"""
https://leetcode.com/problems/valid-anagram/description/
----
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sdict, tdict = {}, {}

        for char in s:
            if char not in sdict:
                sdict[char] = 1
            else:
                sdict[char] += 1

        for char in t:
            if char not in tdict:
                tdict[char] = 1
            else:
                tdict[char] += 1

        for char in sdict:
            if char not in tdict:
                return False
            elif tdict[char] != sdict[char]:
                return False
            _ = tdict.pop(char)

        if len(tdict) != 0:
            return False

        return True
