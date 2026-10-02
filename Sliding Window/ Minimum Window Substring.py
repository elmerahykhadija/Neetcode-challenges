"""
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        left=0
        right=0
        mini=""
        d={}
        for i in t:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        while right < len(s):
            if s[right] in d:
                d[s[right]]-=1
            while all(value<=0 for value in d.values()):
                if mini=="" or len(mini)>right-left+1:
                    mini=s[left:right+1]
                    
                if s[left] in d:
                    d[s[left]]+=1
                left+=1  
                
            right+=1
        return mini

            
            