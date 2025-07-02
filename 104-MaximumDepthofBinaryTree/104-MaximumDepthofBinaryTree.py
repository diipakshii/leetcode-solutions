# Last updated: 7/1/2025, 11:12:26 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # breath first search -> O(n)
        if not root:
            return 0
        
        level = 0
        
        # initialize queue with root
        queue = deque([root])

        # keep going until queue is empty
        while queue:
            # remove what is current nodes in queue and add children
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return level

        