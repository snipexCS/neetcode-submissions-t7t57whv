# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            local_queue = []
            for _ in range(level_length):
                value =  queue.popleft()
                local_queue.append(value.val)
                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)
            
            level.append(local_queue)
        
        return level
            
        
        
        
        return queue

            

                



        