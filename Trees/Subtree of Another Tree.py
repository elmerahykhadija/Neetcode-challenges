"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

exemple 1:
Input: root = [1,2,3,4,5], subRoot = [2,4,5]
Output: true

exemple 2:
Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
Output: false
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and not subRoot:
            return True
        if not root and subRoot :
            return False
        def compare(root,subRoot):
            if root.val!=subRoot.val:
                return False
            s1=[root]
            s2=[subRoot]
            while s1 and s2 :
                n1=s1.pop()
                n2=s2.pop()
                if n1.val!=n2.val:
                    return False
                if n1.left and n2.left:
                    if n1.left.val==n2.left.val:
                        s1.append(n1.left)
                        s2.append(n2.left)
                    else: 
                        return False
                elif n1.left or n2.left:
                    return False
                if n1.right and n2.right:
                    if n1.right.val==n2.right.val:
                        s1.append(n1.right)
                        s2.append(n2.right)
                    else: 
                        return False
                elif n1.right or n2.right:
                    return False

            return True
        
        if root.val==subRoot.val:
            if compare(root,subRoot):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
                