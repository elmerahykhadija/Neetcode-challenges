'''
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.


'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        resultat=[]
        for i in range(0,len(temperatures)):
            resultat.append(0)
        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                a=stack.pop()
                resultat[a]=i-a
            stack.append(i)
        
        return resultat
        
        
        