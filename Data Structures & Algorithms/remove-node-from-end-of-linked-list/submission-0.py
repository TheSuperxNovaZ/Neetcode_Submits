# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self,head: Optional[ListNode],n: int) -> Optional[ListNode]:
        if not head:
            return None
        # Reverse the list
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # prev is now the head of the reversed list
        # The nth node from the end is now the nth node from the start
        dummy = ListNode(0)
        dummy.next = prev
        curr = dummy
        # Move to the node BEFORE the one we want to remove
        for _ in range(n - 1):
            curr = curr.next
        # Remove nth node
        curr.next = curr.next.next

        # Reverse the list back
        prev = None
        curr = dummy.next

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev