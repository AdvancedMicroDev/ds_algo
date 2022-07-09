# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Edge case: List is null or empty LL
        Variable lists contains K no. of Lists
        """
        if not lists or len(lists) == 0:
            return None

        """
        Hard Part: Take pairs of LL & Merge them each time
        Keep doing this until only one List remains, 
        this list is our output
        """
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                # Taking 2 lists at a time
                # l1 & l2
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        # Similar to merge 2 LL
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next
