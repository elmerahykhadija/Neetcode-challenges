"""
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Input: heights = [7,1,7,2,2,4]

Output: 8
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxi=0
        stack=[]
        for i,h in enumerate(heights):
            if not stack:
                stack.append((i,h))
            else:
                j=i
                while stack and  stack[-1][1] >= h:
                    a,b=stack.pop()
                    aire = b * (i - a)
                    maxi = max(maxi, aire)  
                    j=a
                stack.append((j,h))
                
        while stack :
            v=(len(heights)-stack[-1][0])*stack[-1][1]
            maxi=max(maxi,v)
            stack.pop()
        return maxi





        