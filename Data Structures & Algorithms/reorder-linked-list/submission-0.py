# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        lis = []
        while curr:
            lis.append(curr)
            curr = curr.next

        n = len(lis)
        new = []

        forw = 0
        rev = n - 1
        for i in range(n):
            if i % 2 == 0:
                new.append(lis[forw])
                forw += 1
            else:
                new.append(lis[rev])
                rev -= 1
        for i in range(n - 1):
            new[i].next = new[i + 1]

        new[-1].next = None
        