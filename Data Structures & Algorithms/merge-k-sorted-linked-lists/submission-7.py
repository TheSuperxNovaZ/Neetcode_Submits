class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        master = []
        for lis in lists:
            curr = lis
            while curr:
                master.append(curr.val)
                curr = curr.next
        master.sort()
        dummy = ListNode()
        curr = dummy
        for val in master:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next