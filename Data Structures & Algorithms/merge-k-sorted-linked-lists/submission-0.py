# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeLists(self, l1, l2):
        dummy = ListNode(-1)
        temp = dummy
        first, sec = l1, l2
        while first and sec:
            if first.val < sec.val:
                temp.next = first
                first = first.next
            else:
                temp.next = sec
                sec = sec.next
            temp = temp.next
        
        while first:
            temp.next = first
            first = first.next
            temp = temp.next
        
        while sec:
            temp.next = sec
            sec = sec.next
            temp = temp.next
        
        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeLists(list1, list2))
            lists = mergedLists
        
        return lists[0]

        