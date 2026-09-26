# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, current = None, slow.next
        slow.next = None
        while current:
            print("reversing the list")
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        first_list, second_list = head, prev
        while second_list:
            print("reordering")
            first_temp, second_temp = first_list.next, second_list.next
            first_list.next = second_list
            second_list.next = first_temp
            first_list = first_temp
            second_list = second_temp
        

        