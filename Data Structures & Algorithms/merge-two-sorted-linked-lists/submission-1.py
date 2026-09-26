# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge_recursive(self, head1, head2, tail):
        if not head1: 
            tail.next = head2
            return
        if not head2: 
            tail.next = head1
            return
        if head1.val < head2.val:
            tail.next = head1
            head1 = head1.next
            tail = tail.next
        else:
            tail.next = head2
            head2 = head2.next
            tail = tail.next
        return self.merge_recursive(head1, head2, tail)



    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        self.merge_recursive(list1, list2, tail)
        return dummy.next
        