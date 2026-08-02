"""
Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        liste=[]
        while head :
            liste.append(head)
            head=head.next
        dummy=ListNode()
        current=dummy
        for i in range(0,len(liste)):
            if i != len(liste)-n:
                current.next=liste[i]
                current=current.next
        current.next=None
        return dummy.next