"""
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.


Example 1:

Input: s = "zxyzxyz"

Output: 3
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        l = 0
        d = {}
        while left <=right and right <len(s):
            if s[right] in d :
                left=max(left,d[s[right]]+1)
            d[s[right]]=right
            l=max(l,right-left+1)
            right+=1
        return l

