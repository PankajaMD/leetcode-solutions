# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        min_heap = []
        for list_node in lists:
            while list_node is not None:
                heapq.heappush(min_heap, list_node.val)
                list_node = list_node.next

        dummy = ListNode(1)
        merge = dummy
        while min_heap:
            merge.next = ListNode(heapq.heappop(min_heap))
            merge = merge.next

        return dummy.next 
