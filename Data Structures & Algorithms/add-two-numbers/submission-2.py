# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""
        while l1:
            str1+=str(l1.val)
            l1 = l1.next
      

        while l2:
             str2+=str(l2.val)
             l2 = l2.next

        
        

        rev1 = int(str1[::-1])
        rev2 = int(str2[::-1])

        
        result = rev1+rev2

        modifiedStr =  str(result)[::-1]

        head = ListNode(int(modifiedStr[0]))
        cur = head

        modifiedStr =  str(result)[::-1]
        for char in modifiedStr[1:]:
            cur.next = ListNode(int(char))
            cur = cur.next
        
        return head
           


        


        
        
        