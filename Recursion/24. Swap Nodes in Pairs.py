class Solution:
    def swaprec(self, prev: ListNode, curr: ListNode) -> None:
        if not curr or not curr.next:
            return

        f = curr
        s = curr.next

        f.next = s.next
        s.next = f
        prev.next = s

        self.swaprec(f, f.next)

    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        dummy.next = head

        self.swaprec(dummy, head)

        return dummy.next