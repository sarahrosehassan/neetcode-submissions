# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Brute force: visit every single node in the tree to check validity

        # Optimized: Pass a range down
        # Each node checks itself against that range
        # Update the range when we go left or right
        
        # Define a helper function that takes a node, min, and max
        # Base case: if node is null, return True (empty tree is valid)
        # Check if node.val is within (min, max), if not return False
        # Recurse left: update max to node.val
        # Recurse right: update min to node.val
        # Return True only if both left and right are valid

        # Time O(n) Space: O(n)

        def helper(node, min,  max):
            if node == None:
                return True
            if not (min < node.val < max):
                return False
                
            return (helper(node.left, min, node.val) and helper(node.right, node.val, max))
            
        return helper(root, float('-inf'), float('inf')) 

