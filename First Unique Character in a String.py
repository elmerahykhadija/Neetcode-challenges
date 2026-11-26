""" You are given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "neetcodeislove"

Output: 0"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i,c in enumerate(s):
            if c in d :
                d[c][1]+=1
            else:
                d[c]=[i,1]
        onlyOnce=[]
        for i in d:
            if d[i][1]==1:
                onlyOnce.append(d[i])
        onlyOnce.sort()
        if len(onlyOnce)==0:
            return -1
        return onlyOnce[0][0]
