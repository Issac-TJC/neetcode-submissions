# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxn = root.val
        res = [0]
        def dfs(node, maxn):
            if not node:
                return
            if maxn <= node.val:
                res[0] += 1
                maxn = node.val
            dfs(node.left, maxn)
            dfs(node.right, maxn)
        dfs(root, maxn)
        return res[0]
        