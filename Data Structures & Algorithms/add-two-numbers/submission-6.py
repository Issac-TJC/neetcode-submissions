# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        of = 0
        cur = dummy = ListNode()
        while l1 or l2:
            if not l1:
                total = 0 + l2.val + of
            elif not l2:
                total = 0 + l1.val + of
            else:
                total = l1.val + l2.val + of
            if total >= 10:
                node = ListNode(val=total%10)
                of = 1
                cur.next = node
                cur = node
                l1 = l1.next if l1 else l1
                l2 = l2.next if l2 else l2
                continue
            node = ListNode(val=total)
            of = 0
            cur.next = node
            cur = node
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if of:
            node = ListNode(val=1)
            cur.next = node
        return dummy.next
        