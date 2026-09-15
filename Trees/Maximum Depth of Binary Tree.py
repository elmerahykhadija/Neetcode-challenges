"""
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [1,2,3,null,null,4]
Output: 3

Example 2:
Input: root = []
Output: 0
"""
# METHODE 1 BFS -----------------------
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        q=deque([root])
        n=0
        while q:
            lenght=len(q)
            for _ in range(lenght):

                node=q.popleft()
                if node.left :
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            n+=1
        return n
#METHODE 2 DFS -----------------------
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        stack=[(root,1)]
        maximum=0
        while stack:
            node,depth=stack.pop()
            maximum=max(maximum,depth)
            if node.left:
                stack.append((node.left,depth+1))
            if node.right:
                stack.append((node.right,depth+1))
        return maximum
#METHODE 3 RECURSIVE -----------------------
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        return 1+max(left,right)