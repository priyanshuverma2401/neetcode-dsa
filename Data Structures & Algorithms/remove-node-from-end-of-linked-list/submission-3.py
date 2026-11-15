# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None
        total_node = 0
        temp = head
        while temp:
            temp = temp.next
            total_node+=1

        if total_node == 1 and n == 1: return None
        if n == total_node: return head.next
        print(f"Total Number of node: {total_node}")

        target_node = total_node - n

        temp = head
        curr = 0
        while curr < target_node - 1:
            temp = temp.next
            curr+=1
        
        temp.next = temp.next.next
        return head


        