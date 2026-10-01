class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(1)
        merge = dummy
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                merge.next = list1
                list1 = list1.next
            else:
                merge.next = list2
                list2 = list2.next
            merge = merge.next
        if list1 == None:
            merge.next = list2
        else:
            merge.next = list1
        
        return dummy.next
