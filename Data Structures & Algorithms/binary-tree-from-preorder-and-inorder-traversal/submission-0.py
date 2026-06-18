# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.i = 0
        def dfs(l, r):
            if l > r:
                return None
            
            valRoot = preorder[self.i]
            self.i += 1
            root = TreeNode(valRoot)
            root.left = dfs(l, indices[valRoot]-1)
            root.right = dfs(indices[valRoot]+1, r)
            return root
        
        return dfs(0, len(inorder) - 1)
        