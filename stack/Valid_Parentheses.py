"""Valid Parentheses.

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:
- Every open bracket is closed by the same type of close bracket.
- Open brackets are closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        d={ 
            ')':'(', 
            ']':'[', 
            '}':'{'
             }
        stack=[]
        ref=list(s)
        for i in s:
            if i in "([{":
                stack.append(i)
            else :
                if not stack :
                    return False
                a=stack.pop()
                if d[i]!=a:
                    return False
        if not stack :
            return True
        else :
            return False
#------------------------------------------------------------
#------METHOD 2-----------------------------------------

class Solution:
    def isValid(self, s: str) -> bool:
        hash_map={
            '(':')',
            '[':']',
            '{':'}'
        }
        count=0
        stack=[]
        for i in s:
            if i in hash_map:
                stack.append(i)
            else:
                if not stack : return False
                if stack[-1] in hash_map and hash_map[stack[-1]]==i:
                    stack.pop()
                    count+=1
                else:
                    return False
        if stack:
            return False
        if count==len(s)//2:
            return True



        
