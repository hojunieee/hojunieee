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
        
        while rabbit!= None and rabbit.next != None:
            rabbit = rabbit.next.next
            turtle = turtle.next
            if rabbit == turtle:
                return True
        return False
            