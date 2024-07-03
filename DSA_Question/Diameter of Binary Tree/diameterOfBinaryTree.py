class TreeNode:
    def __init__(self,val = 0,left = None, right = None):
        self.value = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self,rootNode:TreeNode)->int:
        res = [0]        
        def dfs(rootNode):
            if not rootNode:
                return -1
            left = dfs(rootNode.left)
            right = dfs(rootNode.right)
            res[0] = max(res[0],left+right+2)

            return 1+max(left,right)
        dfs(rootNode)
        return res[0]