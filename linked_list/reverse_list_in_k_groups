# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.getKth(groupPrev, k)
            
            if not kth:
                break
            groupNext = kth.next
            
            # reverse group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext: # groupNext is similar to prev
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
            # MOST DIFFICULT PART -> Changing the starting pointer
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next
            

    # Helper function to get the kth node   
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        