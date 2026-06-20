# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = ""
        def dfs(root):
            if not root:
                self.res += "#"
                return
            self.res += str(root.val)
            self.res += "#"
            dfs(root.left)
            dfs(root.right)
            self.res += "/"
            return
        dfs(root)
        return self.res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        def dfs():
            if data[self.i] == "#":
                self.i += 1
                return None
            now = ""
            while data[self.i] != "#":
                now += data[self.i]
                self.i += 1
            self.i += 1
            node = TreeNode(int(now))
            node.left = dfs()
            node.right = dfs()
            self.i += 1
            return node
        return dfs()
