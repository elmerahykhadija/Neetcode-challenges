"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1=list1
        c2=list2
        temp=ListNode()
        head=temp
        while c1 and c2 :
            if c1.val>=c2.val:
                head.next=c2
                c2=c2.next
            else :
                head.next=c1
                c1=c1.next
            head=head.next
        if c1:
            head.next=c1
        else:
            head.next=c2
        
        return temp.next
            



        