# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find(self, root, p, q, n):
        if not root:
            return 0
        left = self.find(root.left, p, q, n)
        right = self.find(root.right, p, q, n)
        if left == 2 or right == 2:
            return 2
        if root.val == p.val or root.val == q.val:
            total = 1 + left + right
        else:
            total = left + right

        if total == 2:
            n.append(root)
        
        return total

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        n = []
        t = self.find(root, p, q, n)
        node = n.pop()
        return node
        