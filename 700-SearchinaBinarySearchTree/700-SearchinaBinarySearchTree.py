# Last updated: 7/19/2025, 1:41:50 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        while root is not None and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        
        return root
            
        