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
