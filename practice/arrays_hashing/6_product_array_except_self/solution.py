"""
https://leetcode.com/problems/product-of-array-except-self/description/
----
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        snums = len(nums)
        prefixs = [1 for _ in range(snums)]
        acc_prefix = 1
        for idx in range(snums):
            num = nums[idx]
            prefixs[idx] = acc_prefix * num 
            acc_prefix *= num

        suffixs = [1 for _ in range(snums)]
        acc_suffix = 1
        for idx in reversed(range(snums)):
            num = nums[idx]
            suffixs[idx] = acc_suffix * num 
            acc_suffix *= num

        answer = [1 for _ in range(snums)]
        for idx in range(len(nums)):
            if idx == 0:
                answer[idx] = 1 * suffixs[idx+1]

            elif idx < (snums-1):
                answer[idx] = prefixs[idx - 1] * suffixs[idx + 1]

            else:
                answer[idx] = prefixs[idx-1] * 1

        return answer

    def productExceptSelfLessMemory(self, nums: List[int]) -> List[int]:


        output = [1 for _ in range(len(nums))] 

        acc = 1

        for idx, num in enumerate(nums):
            output[idx] = acc * num 
            acc *= num 

        acc = 1
        idx = len(output) - 1 
        for num in nums[::-1]:
            if idx == (len(nums)-1):
                output[idx] = 1 * output[idx-1]
                acc *= num
            elif idx == 0:
                output[idx] = acc
            else:
                output[idx] = output[idx-1] * acc
                acc *= num
            idx -= 1

        return output

result = Solution().productExceptSelfLessMemory([1,2,3,4])
print(result)
