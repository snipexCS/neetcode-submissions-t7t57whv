# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        result = []
        

        while queue:
            length = len(queue)
            for i in range(length ):
                value = queue.popleft()
                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)
                
                if i == length - 1:
                    result.append(value.val)
                    
        return result






        