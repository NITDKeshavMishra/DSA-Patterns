# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: ListNode, size: int) -> ListNode:
        curr = head
        prev = None

        while size:
            nexti = curr.next
            curr.next = prev
            prev = curr
            curr = nexti
            size -= 1

        return prev

    def reverseKGroup(
        self, head: ListNode | None, k: int
    ) -> ListNode | None:
        if head is None or k <= 1:
            return head

        dummy = ListNode(0, head)
        prevleft = dummy
        left = head

        while left:
            # Check if k nodes are available
            group_end = left
            count = 1

            while count < k and group_end:
                group_end = group_end.next
                count += 1

            # If fewer than k nodes remain, do not reverse
            if group_end is None:
                break

            # Save node after this group
            nextleft = group_end.next

            # Reverse exactly k nodes
            new_head = self.reverse(left, k)

            # Connect previous group to reversed group
            prevleft.next = new_head

            # Connect reversed group to remaining list
            left.next = nextleft

            # Move to next group
            prevleft = left
            left = nextleft

        return dummy.next