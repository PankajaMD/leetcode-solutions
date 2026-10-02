class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(1)
        dummy.next = head
        front = dummy
        back = dummy

        for i in range(n + 1):
            front = front.next

        while front is not None:
            front = front.next
            back = back.next

        back.next = back.next.next

        return dummy.next
