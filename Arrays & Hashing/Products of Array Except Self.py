"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
"""
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*len(nums)
        
        #calculate the left product 
        left_product=1
        for i in range(0,len(nums)):
            output[i]*=left_product
            left_product=left_product*nums[i]
        #calculate the right product
        right_product=1
        i=len(nums)-1
        while i < len(nums) and i >=0:
            output[i]*=right_product
            right_product=right_product*nums[i]
            i=i-1
        return output
        
        