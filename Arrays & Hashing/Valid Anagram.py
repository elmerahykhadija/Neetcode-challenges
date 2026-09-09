"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.


Example 1:

Input: s = "racecar", t = "carrace"

Output: true
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if len(s)==0:
            return False
        d={}
        #Calculate the number of character appearing in s
        for i in s: 
            if i in d:
                d[i]=d[i]+1
            else :
                d[i]=1
        for j in t :
            if j in d : 
                d[j]=d[j]-1
            else :
                return False
        for k in d.values() :
            if k !=0:
                return False
        return True

        