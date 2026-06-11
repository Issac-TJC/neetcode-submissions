# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, root, n):
        if not root:
            return 0
        left = self.depth(root.left, n)
        right = self.depth(root.right, n)
        n[0] = n[0] if n[0] > (left+right) else (left+right)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        n = [0]
        depth = self.depth(root, n)
        return n[0]
        