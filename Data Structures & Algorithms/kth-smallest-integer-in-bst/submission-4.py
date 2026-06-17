# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k]
        def dfs(root):
            if not root:
                return False
            if dfs(root.left):
                return True
            count[0] -= 1
            if count[0] == 0:
                count[0] = root.val
                return True
            if dfs(root.right):
                return True
            return False
        dfs(root)
        return count[0]

        