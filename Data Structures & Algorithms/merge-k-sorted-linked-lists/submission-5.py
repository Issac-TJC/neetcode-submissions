# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# define a wrapper class to tell heapq how to compare complex data structure
class NodeWrapper:
    def __init__(self, node):
        self.node = node

    # define less than
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        dummy = cur = ListNode()
        # use a normal list to manage heap
        minHeap = []

        for lst in lists:
            if lst:
                heapq.heappush(minHeap, NodeWrapper(lst))
        
        while minHeap:
            now = heapq.heappop(minHeap)
            cur.next = now.node
            cur = cur.next

            if now.node.next:
                heapq.heappush(minHeap, NodeWrapper(now.node.next))

        return dummy.next
        