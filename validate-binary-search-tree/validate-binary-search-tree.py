# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Define a helper function that performs an in-order traversal of the tree.
        def in_order_traversal(node):
            # If the node is None (i.e., we've reached a leaf node), return an empty list.
            if not node:
                return []
            
            # Perform an in-order traversal: left child -> node -> right child.
            # Concatenate the values into a single list and return it.
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
        
        # Call the helper function to get a list of node values from the in-order traversal.
        values = in_order_traversal(root)
        
        # Check if the list of values is sorted. If it is, then the tree is a valid BST.
        # The 'all' function returns True if all values in the iterable (the generator expression here) are True.
        return all(values[i] < values[i+1] for i in range(len(values) - 1))
        
        