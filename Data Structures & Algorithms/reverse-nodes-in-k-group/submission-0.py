# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        count = k
        stack = []
        dummy = slow = ListNode()
        fast = head
        while fast:
            stack.append(fast)
            count -= 1
            tmp = fast.next
            if count == 0:
                while stack:
                    now = stack.pop()
                    slow.next = now
                    slow = slow.next
                slow.next = tmp
                count = k
            fast = tmp
        return dummy.next
        