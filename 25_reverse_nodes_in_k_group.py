# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        ptr = head
        ktail = None
        new_head = None

        while ptr is not None:
            count = 0
            ptr = head

            while count < k and ptr is not None:
                ptr = ptr.next
                count += 1

            if count == k:
                rev_head = self.reverseLinkedList(head, k)

                if new_head is None:
                    new_head = rev_head

                if ktail is not None:
                    ktail.next = rev_head

                ktail = head
                head = ptr

        if ktail is not None:
            ktail.next = head

        return head if new_head is None else new_head

    def reverseLinkedList(self, head: ListNode, k: int) -> ListNode:
        new_head = None
        ptr = head

        while k > 0:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = next_node
            k -= 1

        return new_head
