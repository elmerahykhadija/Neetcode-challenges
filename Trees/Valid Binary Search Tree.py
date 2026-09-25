"""
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.

"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values=[]
        def dfs(node):
            if not node :
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
        dfs(root)
        for i in range(len(values)-1):
            if values[i]>=values[i+1]:
                return False
        return True