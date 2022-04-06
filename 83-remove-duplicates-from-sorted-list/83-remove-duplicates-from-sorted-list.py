# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        ans = ListNode(head.val)
        tail = ans
        prev_val = head.val
        current=head.next
        
        while current:
            if current.val != prev_val:
                newnode = ListNode(current.val)
                tail.next = newnode
                tail = newnode
            prev_val = current.val
            current=current.next

        return(ans)