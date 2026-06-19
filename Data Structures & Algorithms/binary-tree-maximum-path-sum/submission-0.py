# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            total = root.val + left + right
            self.maxSum = max(self.maxSum, total)
            now = max(left, right)
            return max(0, now + root.val)
        dfs(root)
        return self.maxSum
        