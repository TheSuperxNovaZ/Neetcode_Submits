import heapq
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Add the first node of each non-empty list
        for i, node in enumerate(lists):
            if node:
                heap.append((node.val, i, node))

        heapq.heapify(heap)

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            # Add the next node from the same list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next