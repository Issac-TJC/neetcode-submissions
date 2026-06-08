# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = ListNode()
        # cur = head
        # flag = 1
        # while cur:
        #     if flag:
        #         cur = cur.next
        #         flag = 0
        #         continue
        #     temp = cur.next
        #     cur.next = node
        #     node = cur
        #     cur = temp
        #     flag = 1
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None
        slow = temp
        
        while slow:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp

        cur = head
        while node.next and cur:
            temp = cur.next
            cur.next = node
            node = node.next
            cur.next.next = temp
            cur = temp
        