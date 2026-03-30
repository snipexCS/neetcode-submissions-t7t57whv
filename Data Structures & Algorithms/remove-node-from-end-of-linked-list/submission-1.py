# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        counter = 0
        length = 0 
        

        while cur:
            length+=1
            cur = cur.next
        
        
        
        cur = head

        if n == length:
            return head.next
            
        
        while counter < (length - n) -1 :
            cur = cur.next
            counter+=1
        
        cur.next = cur.next.next

        return head

        

        

        


        

        