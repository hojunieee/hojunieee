# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None or head.next == None:
            return False
        
        rabbit = head
        turtle = head
                
        while rabbit.next != None and rabbit.next.next != None and rabbit.next.next.next != None:
            rabbit = rabbit.next
            rabbit = rabbit.next
            rabbit = rabbit.next
            turtle = turtle.next
            
            if rabbit.next == turtle.next:
                return True
            
        return False
            