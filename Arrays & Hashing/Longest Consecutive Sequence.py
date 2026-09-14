"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        d={}
        liste=list(set(nums))
        liste.sort()
        i=0
        n=0
        while i <len(liste)-1:
            if (liste[i+1]-liste[i])==1:
                i+=1
            else :
                d[tuple(liste[n:i+1])]=len(liste[n:i+1])
                n=i+1
                i=n
        d[tuple(liste[n:i+1])]=len(liste[n:i+1])
        return max(d.values())
