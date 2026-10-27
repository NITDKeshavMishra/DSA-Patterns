# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swaprec(self, prev: ListNode | None, curr: ListNode | None) -> ListNode | None:
        # When curr becomes None, prev is the new head
        if curr is None:
            return prev

        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

        return self.swaprec(prev, curr)

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        return self.swaprec(None, head)