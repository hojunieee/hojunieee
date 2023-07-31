# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Handle exception: Case when tree is empty
        if not root:
            return []
        
        # Initialize
        queue =[root]
        ans =[]
        
        while len(queue)>0:
            level = []
            # Iterate n times when n is # of element on that layer
            for i in range(len(queue)):
                # Save that element
                node = queue.pop(0)
                level.append(node.val)
                # Add next layer to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Save each layer
            ans.append(level)
        return ans