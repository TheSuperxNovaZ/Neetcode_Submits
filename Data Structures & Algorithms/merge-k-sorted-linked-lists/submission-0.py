class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        master = []

        # Step 1: Collect values from every linked list
        for lis in lists:
            curr = lis
            while curr:
                master.append(curr.val)
                curr = curr.next

        # Step 2: Sort all values
        master.sort()

        # Step 3: Build the merged linked list
        dummy = ListNode(0)
        curr = dummy

        for value in master:
            curr.next = ListNode(value)
            curr = curr.next

        return dummy.next