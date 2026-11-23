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
#method 1: using postfix and prefix product
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        postfix=[1]*len(nums)
        output=[]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            postfix[i]=postfix[i+1]*nums[i+1]
        
        for j in range(0,len(nums)):
            output.append(postfix[j]*prefix[j])
        return output
#method 2: import math
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
        


        