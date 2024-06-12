# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict, deque
        result = []
        if not root:
            return result
        height = 0
        d = deque()
        dd = defaultdict(list)
        d.append((root,0))
        while d:
            node, level = d.popleft()
            
            if node:
                dd[level].append(node.val)
                d.append((node.left, level +1))
                d.append((node.right, level +1))
                height = max(height, level)
        else:
            for i in range(height+1):
                result.append(dd[i])
        return result
