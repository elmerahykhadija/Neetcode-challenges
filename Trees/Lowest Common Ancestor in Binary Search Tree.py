"""
Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q are descendants. The ancestor is allowed to be a descendant of itself
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
Output: 5
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root :
            return 
        if root.val > p.val and root.val > q.val :
            return self.lowestCommonAncestor(root.left,q,p)
        elif root.val < p.val and root.val < q.val :
            return self.lowestCommonAncestor(root.right,q,p)
        else:
            return root

        