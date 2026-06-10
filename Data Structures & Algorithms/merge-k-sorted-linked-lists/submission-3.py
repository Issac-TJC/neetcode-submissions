# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        have = len(lists)
        empty = set()
        while have:
            minHead = ListNode(val=float('inf'))
            mini = 0
            for i in range(len(lists)):
                if i in empty:
                    continue
                if not lists[i]:
                    empty.add(i)
                    have -= 1
                    continue
                if minHead.val > lists[i].val:
                    minHead = lists[i]
                    mini = i
            cur.next = minHead
            if minHead.next:
                lists[mini] = minHead.next
            else:
                empty.add(mini)
                have -= 1
            cur = cur.next
        return dummy.next
        