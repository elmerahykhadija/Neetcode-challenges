"""

You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left <=right :
            mid= (left+right)//2
            if target == nums[mid] :
                return mid 
            if nums[mid-1]<nums[mid]:
                if target in nums[left:mid]:
                    right=mid-1
                else :
                    left = mid+1
            else :
                if target in nums[mid+1:right+1]:
                    left=mid+1
                else :
                    right=mid-1
        return -1
            


        
                


        
        