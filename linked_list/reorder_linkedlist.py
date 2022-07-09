# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        # Increase fast till it is not null or
        # reached the end of the list
        while fast and fast.next:
            # shift slow by one and fast by 2
            slow = slow.next
            fast = fast.next.next

        """
        Second half list begins when above
        loop ends and slow.next points to 
        first element in 2nd half list
        """
        second = slow.next
        """
        slow.next = end of final list
        hence, set it to null. Also,
        set previous to none
        """
        prev = slow.next = None

        # Reverse 2nd half list
        """
        1>2>|3>4| 3,4 are in 2nd half.
        second = 3, prev = None
        """
        while second:
            """
            tmp = 4 | None
            second.next = None | 3
            prev = 3 [second] | 4
            second = tmp = 4 | None
            """
            tmp = second.next  # Store original link in tmp
            second.next = prev  # Reversing starts
            prev = second
            second = tmp

        # Merge both lists
        first, second = head, prev  # head = 1, prev = 4
        while second:
            """
            Store OG next links in tmp1 and tmp2
            tmp = 
            f = 1
            s = 4
            tmp1 = 2
            tmp2 = 3
            f.next = 4
            s.next = 2
            f = 2
            s = 3
            final result = 1->4->2->3
            """
            tmp1, tmp2 = first.next, second.next
            first.next = second  # 1>4
            second.next = tmp1
            first = tmp1
            second = tmp2
