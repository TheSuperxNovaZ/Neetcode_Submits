"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        ref = {}
        curr = head
        while curr:
            ref[curr]= Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            ref[curr].next = ref.get(curr.next)
            ref[curr].random = ref.get(curr.random)
            curr= curr.next
        return ref[head]
        return head