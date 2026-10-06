"""
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1=l1
        c2=l2
        out=ListNode(val=0,next=None)
        current=out
        carry=0
        while c1 or c2 or carry:
            if c1 and c2 : 
                s=c1.val+c2.val+carry
            elif c1 and not c2:
                s=c1.val+carry
            elif c2 and not c1:
                s=c2.val+carry
            elif not c1 and not c2 :
                s=carry
            val=s%10
            node=ListNode(val=val,next=None)
            carry=s//10
            current.next=node
            
            if c1 : c1=c1.next
            if c2 : c2=c2.next
            current=current.next
        
        return out.next

        