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

        # copy nodes into the same list
        cur = head
        while cur:
            node = Node(cur.val)
            temp = cur.next
            cur.next = node
            node.next = temp
            cur = temp

        # split two list
        org = head
        copy = head.next
        dummy = Node(0)
        dummy.next = copy

        # # get the copy list
        # while copy and copy.next:
        #     copy.random = org.random.next if org.random else None
        #     org = copy.next
        #     copy.next = org.next
        #     copy = copy.next
        
        # # last copy node
        # copy.random = org.random.next if org.random else None
        # copy.next = None

        # copy random first:
        while copy and copy.next:
            copy.random = org.random.next if org.random else None
            org = copy.next
            copy = org.next
        
        # last copy node
        copy.random = org.random.next if org.random else None

        # split two list:
        org = head
        copy = dummy.next
        while copy and copy.next:
            org.next = copy.next
            org = org.next
            copy.next = org.next
            copy = copy.next
        
        org.next = None
        
        return dummy.next
        