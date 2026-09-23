"""
You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.
Input: root = [1,2,3,null,4,null,5]

Output: [1,3,5]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        if not root :
            return []
        q=deque([root])
        while q :
            l=len(q)
            for i in range(l):
                node=q.popleft()
                if i==l-1:
                    output.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)      
        return output 