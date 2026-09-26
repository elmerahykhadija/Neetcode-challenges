"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase=s.lower()
        alphanumeric=""
        for c in phrase:
            if c.isalnum():
                alphanumeric+=c
        left=0
        right=len(alphanumeric)-1
        count=0
        while left<right:
            if alphanumeric[left]==alphanumeric[right]:
                count+=1
                left+=1
                right-=1
            else:
                return False
        return True

