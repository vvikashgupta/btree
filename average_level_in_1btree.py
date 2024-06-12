# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import defaultdict , deque
        if not root:
            return 0
        levels = defaultdict(list)
        sum_list = []
        queue = [(root,1)]
        level = 0 
        while queue:
            node , level = queue.pop(0)
            levels[level].append(node.val)
            if node.left:
                queue.append((node.left , level+1))
            if node.right:
                queue.append((node.right , level + 1))
       
        for k , v in levels.iteritems():
            sum_list.append(float(sum(v))/float(len(v)))
        return sum_list
