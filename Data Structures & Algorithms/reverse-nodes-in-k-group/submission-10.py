class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        master = []
        curr = head
        while curr:
            master.append(curr)
            curr = curr.next
        result = []
        for i in range(0,len(master),k):
            group = master[i:i+k]
            if len(group)==k:
                result.extend(group[::-1])
            else:
                result.extend(group)
        for i in range(len(result)-1):
            result[i].next = result[i+1]
        result[-1].next = None
        return result[0]
