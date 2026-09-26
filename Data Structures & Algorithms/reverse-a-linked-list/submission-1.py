# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, prev, current):
        if not current: return prev
        temp = current.next
        current.next = prev
        prev = current
        current = temp
        return self.reverse(prev, current)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(None, head)
        