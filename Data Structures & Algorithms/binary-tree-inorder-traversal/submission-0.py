# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        def inorderTraversal(node):
            nonlocal visited
            if not node:
                return []
            inorderTraversal(node.left)
            visited.append(node.val)
            inorderTraversal(node.right)
            
        

        inorderTraversal(root)
        return visited
        

        
        