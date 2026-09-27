"""
You are given an integer array heights where heights[i] represents the height of the 
ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxi=0
        while left < right :
            h= min(heights[left],heights[right])
            l=right-left
            maxi=max(l*h,maxi)
            if heights[left] < heights[right]:
                left+=1
            else :
                right-=1
        return maxi


