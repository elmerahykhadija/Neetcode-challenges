"""
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
exemple 1:
Input: p = [1,2,3], q = [1,2,3]

Output: true
exemple 2:
Input: p = [4,7], q = [4,null,7]

Output: false
"""
#METHODE 1: Depth First Search (DFS) 
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q :
            return True
        if (not p and q) or (p and not q):
            return False
        if p.val != q.val :
            return False
        s1=[p]
        s2=[q]
        while s1 and s2:
            n1=s1.pop()
            n2=s2.pop()
            if n1.left and n2.left:
                if n1.left.val != n2.left.val:
                    return False
                s1.append(n1.left)
                s2.append(n2.left)
            elif (n1.left and not n2.left) or (not n1.left and  n2.left):
                return False
            if n1.right and n2.right:
                if n1.right.val != n2.right.val:
                    return False
                s1.append(n1.right)
                s2.append(n2.right)
            elif (n1.right and not n2.right) or (not n1.right and  n2.right):
                return False
        return True
            

#METHODE 2: Recursion
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q :
            return True
        if (not p and q) or (p and not q):
            return False
        if p.val != q.val :
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

#METHODE 3: Breadth First Search (BFS)
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q :
            return True
        if (not p and q) or (p and not q):
            return False
        if p.val != q.val :
            return False
        f1=deque([p])
        f2=deque([q])
        while f1 and f2 :
            n1=f1.popleft()
            n2=f2.popleft()
            if n1.left and n2.left:
                if n1.left.val != n2.left.val:
                    return False
                f1.append(n1.left)
                f2.append(n2.left)
            elif (n1.left and not n2.left) or (not n1.left and  n2.left):
                return False
            if n1.right and n2.right:
                if n1.right.val != n2.right.val:
                    return False
                f1.append(n1.right)
                f2.append(n2.right)
            elif (n1.right and not n2.right) or (not n1.right and  n2.right):
                return False
            return True
        

