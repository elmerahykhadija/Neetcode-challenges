"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        output=[]
        apparence=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            apparence.append(d[i])
        apparence.sort(reverse=True)
        
        for a in range(0,k):
            for i in d :
                if d[i]==apparence[a] and i not in output:
                    output.append(i)
                    break
        return output
            