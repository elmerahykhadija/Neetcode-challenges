"""
You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d={None:None}
        c1=head
        out=Node(x=0,next=None,random=None)
        c=out
        while c1:
            d[c1]=Node(x=c1.val,next=None,random=None)
            c1=c1.next
        c1=head
        while c1:
            n=c1.next
            d[c1].next=d[n]
            r=c1.random
            d[c1].random=d[r]
            c1=c1.next
        
        c1=head
        while c1:
            c.next=d[c1]
            c1=c1.next
            c=c.next
        return out.next

