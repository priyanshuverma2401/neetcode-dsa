# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        head1, head2 = list1, list2
        curr = res
        while head1 and head2:
            if head1.val > head2.val:
                curr.next = ListNode(head2.val)
                head2 = head2.next
            else:
                curr.next = ListNode(head1.val)
                head1 = head1.next
            curr = curr.next
        
        while head1: 
            curr.next = ListNode(head1.val)
            head1 = head1.next
            curr = curr.next
        
        while head2:
            curr.next = ListNode(head2.val)
            head2 = head2.next
            curr = curr.next
        
        return res.next


        