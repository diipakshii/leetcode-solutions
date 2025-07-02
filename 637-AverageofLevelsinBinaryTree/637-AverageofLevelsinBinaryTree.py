# Last updated: 7/1/2025, 11:41:03 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        # BFS -> O(n)
        if not root:
            return []
        
        queue = deque([root])
        averages = []

        while queue:
            sum = 0
            n = len(queue)

            for i in range(n):
                node = queue.popleft()
                sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            averages.append(sum / float(n))
        
        return averages


        