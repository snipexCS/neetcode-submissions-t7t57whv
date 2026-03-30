"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copyNew = {

        }

        cur = head

        while cur:
            copyNew[cur] = Node(cur.val)
            
            cur = cur.next
        
        cur = head

        while cur:
            copy = copyNew[cur]
            copy.random = copyNew.get(cur.random)
            copy.next = copyNew.get(cur.next)
            cur = cur.next
        
        return copyNew[head]
