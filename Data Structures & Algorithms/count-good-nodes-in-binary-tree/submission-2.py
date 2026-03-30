# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNode = 0
        def dfs(node,maxTree):
            nonlocal goodNode
            if not node:
                return 

            if node.val >= maxTree:
                goodNode +=1
            
            newMax = max(maxTree , node.val)
            left = dfs(node.left,newMax)
            right = dfs(node.right,newMax)

        dfs(root,root.val)
        return goodNode
        