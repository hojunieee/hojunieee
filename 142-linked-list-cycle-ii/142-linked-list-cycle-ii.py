# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

    
class Solution:
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return None  
        
        rabbit = head
        turtle = head          
        while rabbit.next != None and rabbit.next.next != None:
            rabbit = rabbit.next
            rabbit = rabbit.next
            turtle = turtle.next    
            if rabbit.next == turtle.next:

                
                keepTrack = list()
                key = head
                
                while key.next != None:
                    if key.next in keepTrack:
                        return key.next
                    else:
                        keepTrack.append(key)
                        key = key.next
        else:
            return None


