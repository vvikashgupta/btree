# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def dfs_tree(root):
            result = []
            if not root:
                return result
            
            result += dfs_tree(root.left)
            result += [root.val]
            result += dfs_tree(root.right)
            return result
        
        def merge_2(lst1, lst2):
            print(merge2)
            result = []
            len1 = len(lst1)
            len2 = len(lst2)
            i = j = 0
            while i < len1 and j < len2:
                if lst1[i] <= lst2[j]:
                    result.append(lst1[i])
                    i += 1
                else:
                    result.append(lst2[j])
                    i += 1
            for k in range(i:len1):
                result.append(lst1[k])
            for k in range(j:len2):
                result.append(lst2[k])
            return result
                    
            
        rlst1 = dfs_tree(root1)
        rlst2 = dfs_tree(root2)
        print(rlst1,rlst2)
        return merge_2(rlst1, rlst2)
            
