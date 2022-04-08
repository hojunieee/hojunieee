# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ansList =list()
        temp = root
        
        def LNRTraversal(temp):
            if temp != None:
                LNRTraversal(temp.left)
                ansList.append(temp.val)
                LNRTraversal(temp.right)

        LNRTraversal(temp)
        
        return ansList