class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        curr = head
        master = []
        while curr:
            master.append(curr)
            curr = curr.next
        n = len(master)
        result = []
        for i in range(0, n, k):
            group = master[i:i + k]
            if len(group) == k:
                result.extend(group[::-1])
            else:
                result.extend(group)
        for i in range(len(result) - 1):
            result[i].next = result[i + 1]
        result[-1].next = None
        return result[0]




