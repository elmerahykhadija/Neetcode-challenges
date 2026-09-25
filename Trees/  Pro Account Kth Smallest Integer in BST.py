"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values=[]
        def dfsInorder(node):
            if node is None:
                return 
            dfsInorder(node.left)
            values.append(node.val)
            dfsInorder(node.right)
        dfsInorder(root)
        return values[k-1]