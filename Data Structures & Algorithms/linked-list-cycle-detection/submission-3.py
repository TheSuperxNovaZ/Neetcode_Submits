# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen = {}
        while curr:
            if curr in seen and curr.next == seen[curr]:
                return True
            seen[curr]=curr.next
            curr = curr.next
        return False
