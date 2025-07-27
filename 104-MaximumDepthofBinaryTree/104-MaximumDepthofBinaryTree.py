# Last updated: 7/27/2025, 12:12:35 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS
        def dfs(node, maximum):
            if not node:
                return 0
            
            if node.val >= maximum:
                good = 1 
            else:
                good = 0

            maximum = max(maximum, node.val)

            good += dfs(node.left, maximum)
            good += dfs(node.right, maximum)

            return good

        return dfs(root, root.val)