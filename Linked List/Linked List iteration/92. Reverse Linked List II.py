# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        
        if head == None:
            return None
        if right == left:
            return head
        
        dummy=ListNode(0,head)
        prev=dummy

        for i in range(left-1):
            prev=prev.next
        
        curr=prev.next
        for i in range(right-left):
            nexti=curr.next
            curr.next=nexti.next
            nexti.next=prev.next
            prev.next=nexti
        
        return dummy.next