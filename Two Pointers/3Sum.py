"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        nums.sort()
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            if i >0 and nums[i]==nums[i-1]:
                continue
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                if s==0 and [nums[i],nums[left],nums[right]] not in output:
                    output.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                elif s<0 :
                    left+=1
                else:
                    right-=1    
        return output               


        