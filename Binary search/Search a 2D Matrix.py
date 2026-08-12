"""
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for liste in matrix:
            left=0
            right=len(liste)-1
            while left<=right:
                mid=(right+left)//2
                if liste[mid]==target:
                    return True
                elif liste[mid] > target:
                    right=mid-1
                else:
                    left=mid+1
        return False
        