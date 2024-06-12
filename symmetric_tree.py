# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        from collections import deque
        d = deque()
        d.append(root)
        d.append(root)
        while d:
            p1 = d.popleft()
            p2 = d.popleft()
            if not p1 and not p2:
                continue
            if not p1 or not p2:
                return False
            if p1.val != p2.val:
                return False
            d.append(p1.left)
            d.append(p2.right)
            d.append(p1.right)
            d.append(p2.left)
        return True

