# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        from collections import deque
        if not root:
            return None
        deq = deque()
        deq.append(root)
        
        while deq:
            node = deq.popleft()
            if not node: continue
            if node.val == val: return node
            elif node.val > val: deq.append(node.left)
            else: deq.append(node.right)
        return None
