"""
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=len(s1)
        left=0
        right=l-1
        
        if len(s1)>len(s2):
            return False
        while right<len(s2) and left<= right:
            d={}
            for i in s1 :
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
            for i in s2[left:right+1]:
                if i in d:
                    d[i]-=1
                else:
                    break
            count=0
            for i in d:
                if d[i]==0:
                    count+=1
            if count==len(d):
                return  True
            left+=1
            right=left+len(s1)-1
        return False