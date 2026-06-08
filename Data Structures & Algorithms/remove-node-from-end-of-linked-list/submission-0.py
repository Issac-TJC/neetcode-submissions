# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 1
        count = {}
        cur = head
        while cur:
            count[l] = cur
            l += 1
            cur = cur.next
        if l-n-1 in count:
            count[l-n-1].next = count[l-n].next
        else:
            head = count[l-n].next
        return head
        