# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Let us explore DFS for the trees ...and check their values
        
        def dfs(root):
            
            ans = []
            if not root:
                return ans
            print(root.val)
            if not root.left and not root.right:
                ans.append(root.val)
            ans += dfs(root.left)
            ans += dfs(root.right)
            print(ans)
            return ans
        return dfs(root1) == dfs(root2)
