"""
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None :
            return
        liste=[]
        current=head
        while current :
            liste.append(current)
            current=current.next
        left=0
        right=len(liste)-1
        dummy=ListNode()
        current=dummy
        while left <= right:
            current.next=liste[left]
            current=current.next
            left=left+1
            if left<=right:
                current.next=liste[right]
                current=current.next
                right=right-1
            current.next=None
        head=dummy.next
            
              
        


        