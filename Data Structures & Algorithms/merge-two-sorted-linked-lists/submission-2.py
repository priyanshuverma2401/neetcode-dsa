# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge_recursive(self, list1, list2):
        if not list1: return list2
        if not list2: return list1
        if list1.val < list2.val:
            list1.next = self.merge_recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_recursive(list1, list2.next)
            return list2
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge_recursive(list1, list2)
        