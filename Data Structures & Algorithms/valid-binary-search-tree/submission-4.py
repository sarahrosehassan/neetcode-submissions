# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # brute force: go to every and check if left, less than parent(and subtrees) check if right, greater than parent(and subtrees)
        # O(n^2)
        # Optimze way: we remember the range each number has to be in

        # helper function dfs checks if the node is valid None return True
        # if the node is not in the valid range we return False
        # initiliaze range to -infinity and +infinity, check of both left and right side along with all subtrees are valid

        def dfs(node, min_val, max_val):
            if node is None:
                return True

            if not (min_val < node.val < max_val):
                return False
                
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        # if we go left, update the max to the current node, if we go right we update the min to the current node
        
        return dfs(root, float('-inf'), float('inf'))



        