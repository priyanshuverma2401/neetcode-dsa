# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kthNode = self.findKthNode(groupPrev, k)
            if not kthNode:
                break
            
            groupNext = kthNode.next
            
            prev, curr = kthNode.next, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = temp
        
        return dummy.next

    def findKthNode(self, root, k):
        while root and k > 0:
            root = root.next
            k-=1
        return root
    


        