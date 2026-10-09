class Solution:
    def removeNthFromEnd(self,head: Optional[ListNode],n: int) -> Optional[ListNode]:
        ref = ListNode(0)
        ref.next = head
        slow = ref
        fast = ref
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return ref.next