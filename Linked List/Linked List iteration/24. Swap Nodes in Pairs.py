# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        
        dummy=ListNode(-1)
        dummy.next=head
        p=dummy

        while head and head.next:
            f=head
            sec=head.next
            f.next=sec.next
            sec.next=f
            p.next=sec

            p=f
            head=f.next

        return dummy.next