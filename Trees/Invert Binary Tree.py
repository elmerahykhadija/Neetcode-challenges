"""
You are given the root of a binary tree root. Invert the binary tree and return its root.

Example 1:
Input: root = [1,2,3,4,5,6,7]

Output: [1,3,2,7,6,5,4]
"""
#METHODE 1 RECURSIVE ---------------------------
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        
        temp=root.left
        root.left=root.right
        root.right=temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

#METHODE 2 BFS  ---------------------------
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return 
     
        q=deque([root])

        while q:
            node=q.popleft()
            temp=node.left
            node.left=node.right
            node.right=temp
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return root
#METHODE 3 DFS ---------------------------
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return 
     
        stack=[root]

        while stack:
            node=stack.pop()
            temp=node.left
            node.left=node.right
            node.right=temp
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        return root
