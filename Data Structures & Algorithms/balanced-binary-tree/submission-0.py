# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, root, n):
        if not root or not n[0]:
            return 0
        left = self.depth(root.left, n)
        right = self.depth(root.right, n)
        if math.fabs(left - right) > 1:
            n[0] = 0
        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        n = [1]
        depth = self.depth(root, n)
        return n[0] == 1
        