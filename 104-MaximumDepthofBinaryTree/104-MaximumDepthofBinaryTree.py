# Last updated: 7/27/2025, 1:08:16 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        else:
            queue = deque([root])
            level = 1
            maximum = root.val
            maxLevel = level

            while queue:
                levelSum = 0

                n = len(queue)

                for i in range(n):
                    node = queue.popleft()
                    levelSum += node.val

                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)

                if levelSum > maximum:
                    maximum = levelSum
                    maxLevel = level

                level += 1

            return maxLevel







        