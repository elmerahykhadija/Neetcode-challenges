"""
You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexes={}
        for i,v in enumerate(inorder):
            indexes[v]=i
        def helper(l,r):
            if l>r:
                return None
            root=TreeNode(preorder.pop(0))
            indx=indexes[root.val]
            root.left=helper(l,indx-1)
            root.right=helper(indx+1,r)
            return root
        return helper(0,len(inorder)-1)