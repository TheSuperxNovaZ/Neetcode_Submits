# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        while l1:
            num1.append(l1.val)
            l1 = l1.next

        while l2:
            num2.append(l2.val)
            l2 = l2.next
        n1 = int(''.join(map(str, num1[::-1]))) if num1 else 0
        n2 = int(''.join(map(str, num2[::-1]))) if num2 else 0
        num3 = str(n1 + n2)[::-1]
        dummy = ListNode(0)
        curr = dummy
        for digit in num3:
            curr.next = ListNode(int(digit))
            curr = curr.next
        return dummy.next

        # dummy = ListNode(0)
        # curr = dummy
        # carry = 0
        # while l1 or l2 or carry:
        #     num1 = l1.val if l1 else 0
        #     num2 = l2.val if l2 else 0
        #     total = num1 + num2 + carry
        #     carry = total // 10
        #     curr.next = ListNode(total % 10)
        #     curr = curr.next
        #     if l1:
        #         l1 = l1.next
        #     if l2:
        #         l2 = l2.next
        # return dummy.next

