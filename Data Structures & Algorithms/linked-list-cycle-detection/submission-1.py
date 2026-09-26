# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import defaultdict
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = defaultdict(bool)
        h = head
        while h:
            if seen[h]: return True
            seen[h] = True
            h = h.next
        return False

        