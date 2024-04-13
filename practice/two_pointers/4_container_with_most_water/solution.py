"""
https://leetcode.com/problems/container-with-most-water/description/
----
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        maxArea = 0

        while r > l:
            x = r - l
            y = min(height[l], height[r])
            guess_area = x*y
            if guess_area > maxArea:
                maxArea = guess_area

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxArea

height = [1,8,6,2,5,4,8,3,7]
result = Solution().maxArea(height)
print(result)
