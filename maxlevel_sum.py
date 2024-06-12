# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxval_level = 0
        maxval = -inf
        from collections import defaultdict, deque
        d = deque()
        leveldict = defaultdict(int)
        d.append((root,0))
        while d:
            node, level = d.popleft()
            if node:
                leveldict[level] += node.val
            if node.left:
                d.append((node.left, level+1))
            if node.right:
                d.append((node.right, level+1))
        else:
            for k,v in leveldict.items():
                if v > maxval:
                    maxval = v
                    maxval_level = k+1
        return maxval_level
