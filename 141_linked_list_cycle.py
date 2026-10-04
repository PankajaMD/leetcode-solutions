# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        slow = head
        fast = head.next

        while slow != None and fast != None:
            if fast.next == None:
                return False
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False

        
