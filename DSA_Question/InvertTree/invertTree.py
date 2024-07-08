class TreeNode:
    def __init__(self, val = 0 , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution :
    def inverTree(self, root: TreeNode()) -> TreeNode():
        if not root:
            return None
        
        temp = root.right
        root.right = root.left
        root.left = temp

        self.inverTree(root.left)
        self.inverTree(root.right)

        return root