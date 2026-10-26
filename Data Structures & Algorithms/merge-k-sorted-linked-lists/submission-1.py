class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        master = []
        for lis in lists:
            curr = lis
            while curr:
                master.append(curr.val)
                curr = curr.next
        master.sort()
        dummy = ListNode(0)
        curr = dummy
        for value in master:
            curr.next = ListNode(value)
            curr = curr.next
        return dummy.next