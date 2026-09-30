"""
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            d={}
            left=0
            right=0
            count=0
            while left <= right and right < len(s):
                if s[right] in d :
                    d[s[right]]+=1
                else:
                    d[s[right]]=1  
                maxi=max(d.values())
                l=len(s[left:right+1])-maxi               
                if l<=k:
                    count=max(count,len(s[left:right+1]))
                else:
                    d[s[left]]-=1
                    left+=1
                right+=1
            return count