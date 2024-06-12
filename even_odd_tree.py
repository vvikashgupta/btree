# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        from collections import deque, defaultdict
        deq = deque()
        deq.append((root,0))
        level_dict = defaultdict(list)
        while deq:
            node, level = deq.popleft()
            level_dict[level].append(node.val)
            if node.left:
                deq.append((node.left, level+1))
            if node.right:    
                deq.append((node.right, level + 1))
        dict_len = len(level_dict)
        for i in range(dict_len):
            if i%2 :
                # Odd index case. All entry should be even and decreasing.
                lst = level_dict[i]
                for index,item in enumerate(lst):
                    if item % 2 == 1:
                        return False
                    elif index != 0 and item >= lst[index-1]:
                        return False
                    else:
                        continue
            else:
                #Even Index Case, All entry should be odd and increasing.
                lst = level_dict[i]
                for index,item in enumerate(lst):
                    if item % 2 != 1:
                        return False
                    elif index != 0 and item <= lst[index-1]:
                        return False
                    else:
                        continue
        return True
