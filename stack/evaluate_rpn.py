"""
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        if len(tokens)==0:
            return 0
        operators=['+','-','*','/']
        stack=[]
        s=0
        for i in tokens:
            if i in operators and stack:
                resultat=stack.pop()
                a=stack.pop()
                if i=='+':
                    s=resultat+a
                elif i=='-':
                    s=a-resultat
                elif i=='*':
                    s=resultat*a
                elif i=='/' and a!=0:
                    s=int(a/resultat)
                stack.append(s)
            else :
                
                stack.append(int(i))
            
        return s
        