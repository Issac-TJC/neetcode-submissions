# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
        head = list1
        cur1 = head
        cur2 = list2
        prev = None
        while cur2:
            while cur1 and cur2.val >= cur1.val:
                prev = cur1
                cur1 = cur1.next
            prev.next = cur2
            cur2 = cur2.next
            prev.next.next = cur1
            prev = prev.next
        return head
