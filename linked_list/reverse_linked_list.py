# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. ITERATIVE SOLUTION:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        
        # 2. RECURSIVE SOLUTION:
#         if not head or not head.next:
#             return head
        
#         newHead = self.reverseList(head.next)
#         nxt = head.next
#         nxt.next = head
#         head.next = None
        
#         return newHead

        