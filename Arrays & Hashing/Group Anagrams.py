"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create an empty dict
        d={}
        #classiffy each str with its sorted caracters tuple 
        for i in strs:
            #create and sort the liste of carcters
            l=list(i)
            l.sort()
            #create the key using tuple 
            key=tuple(l)
            if key in d :
                d[key].append(i)
            else :
                d[key]=[i]
        output=[]
        for k in d:
            output.append(d[k])

        return output
        

        