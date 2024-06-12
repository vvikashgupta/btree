# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        #This is a tree travelsal problem.
        self.maxpath = 0

        def dfs(node, left, step):
            if node:
                self.maxpath = max(self.maxpath, step)
                if left:
                    dfs(node.left, False, step + 1) # Continue current zigzag tree
                    dfs(node.right, True, 1) # Start a new subtree 
                else:
                    dfs(node.left, False, 1)
                    dfs(node.left, True, step+1)
        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.maxpath
