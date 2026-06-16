# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, maxleft, minright):
            if not root:
                return True
            if not dfs(root.left, maxleft, root.val) or not dfs(root.right, root.val, minright):
                return False
            if maxleft < root.val < minright:
                return True
            else:
                return False    
        
        return dfs(root, float("-inf"), float("inf"))
        