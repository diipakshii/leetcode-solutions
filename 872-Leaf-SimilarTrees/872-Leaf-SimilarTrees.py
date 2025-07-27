# Last updated: 7/26/2025, 5:41:13 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isLeaf(root):
    return root and not root.left and not root.right

def solve(root, temp):
    if isLeaf(root):
        temp.append(root.val)
    if root.left:
        solve(root.left, temp)
    if root.right:
        solve(root.right, temp)

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        root1_temp = []
        root2_temp = []

        solve(root1, root1_temp)
        solve(root2, root2_temp)

        return root1_temp == root2_temp
        